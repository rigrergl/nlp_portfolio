const weaviate = require('weaviate-ts-client');
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
            {
                'name': 'longSummary',
                'description': 'Long summary of the chapter',
                'dataType': ['string'],
            },
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
    
    res.status(200);
})

router.post("/write-data", async (req, res, next) => {
    
})

router.get("/get-schema", async (req, res, next) => {
    const schemaRes = await client.schema.getter().do();

    res.json({
        schema: schemaRes
    })
})

module.exports = router;