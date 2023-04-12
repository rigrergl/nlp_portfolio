const weaviate = require('weaviate-ts-client');
const fs = require("fs");
var express = require('express');
var router = express.Router();

const client = weaviate.client({
    scheme: 'http',
    host: 'localhost:8080'
});

router.post("/setup-db", async (req, res, next) => {
    const schemaConfig = {
        'class': 'Chapter',
        'description': 'A chapter of the One Piece manga',
        'vectorizer': 'text2vec-contextionary',
        "vectorIndexType": "hnsw",
        'properties': [
            {
                'name': 'shortSummary',
                'description': 'Short summary of the chapter',
                'dataType': ['string']
            },
            // {
            //     'name': 'longSummary',
            //     'description': 'Long summary of the chapter',
            //     'dataType': ['string'],
            // },
            {
                'name': 'chapterNumber',
                'description': 'The number of the chapter',
                'dataType': ['int'],
                'indexInverted': false // Ignore this property in search and classification
            }
        ],
        "invertedIndexConfig": {
            "stopwords": {
                "preset": "en",
            }
        }
    };

    await client.schema
        .classCreator()
        .withClass(schemaConfig)
        .do();

    res.status(200).send('db successfully setup');
})

router.post("/write-data", async (req, res, next) => {
    try {
        const filePath = './public/kb.json'
        let data = fs.readFileSync(filePath, 'utf8')
        data = JSON.parse(data);

        for (let i = 0; i < 1; i++) {
            const obj = data[i];
            await client.data.creator()
                .withClassName('Chapter')
                .withProperties({
                    shortSummary: obj.short_summary,
                    // longSummary: obj.long_summary,
                    chapterNumber: obj.id
                })
                .do()
            await new Promise(resolve => setTimeout(resolve, 1000)); // Add a delay of 1 second
        }

        res.status(200).send('Objects added to database')
    } catch (err) {
        console.log(err);
        res.status(500).send('Error reading file')
    }
})

router.get("/get-object-count", async (req, res, next) => {
    await client.graphql
        .aggregate()
        .withClassName("Chapter")
        .withFields('meta { count }')
        .do()
        .then(res => {
            console.log(JSON.stringify(res, null, 2))
        })
        .catch(err => {
            console.error(JSON.stringify(err, null, 2))
        });

    res.send(200)
})

router.get("/get-all-objects", async (req, res, next) => {
    await client
        .data
        .getter()
        .withClassName('Chapter')
        .withLimit(2)
        .do()
        .then(res => {
            console.log(res)
        })
        .catch(err => {
            console.error(err)
        });

    res.send(200)
})

router.get("/query", async (req, res, next) => {
    const testText = "luffy meets zoro";

    const resText = await client.graphql.get()
        .withClassName('Chapter')
        .withFields(['shortSummary'])
        .withNearText({concepts: [testText]})
        .withLimit(1)
        .do()
    
    console.log(resText.data.Get.Chapter[0].shortSummary)
})

router.get("/get-schema", async (req, res, next) => {
    const schemaRes = await client.schema.getter().do();
    console.log(schemaRes)
    res.json({
        schema: schemaRes
    })
})

module.exports = router;