const weaviate = require('weaviate-ts-client');
const fs = require("fs");
var express = require('express');
var router = express.Router();

const client = weaviate.client({
    scheme: 'http',
    host: 'localhost:8080'
});

router.post("/load-books", async (req, res, next) => {
    try {
        const filePath = './public/book_summaries.json'
        let data = fs.readFileSync(filePath, 'utf8')
        data = JSON.parse(data);

        for (let i = 0; i < data.length; i++) {
            const obj = data[i];
            console.log(i + "/" + data.length)
            await client.data.creator()
                .withClassName('Book')
                .withProperties({
                    wikipediaArticleId: obj.ID,
                    bookTitle: obj.BookTitle,
                    author: obj.Author,
                    genres: obj.Genres.join(" "),
                    summary: obj.clean_summary
                })
                .do()
        }

        res.status(200).send('Objects added to database')
    } catch (err) {
        console.log(err);
        res.status(500).send('Error reading file')
    }
})

router.delete("/delete-book-class", async (req, res, next) => {
    await client.schema
        .classDeleter()
        .withClassName('Book')
        .do()

    res.status(200).send('Book class deleted')
})

router.delete("/delete-chapter-class", async (req, res, next) => {
    await client.schema
        .classDeleter()
        .withClassName('Chapter')
        .do()

    res.status(200).send('Chapter class deleted')
})

router.post("/setup-book-schema", async (req, res, next) => {
    const schemaConfig = {
        'class': 'Book',
        'description': 'A book',
        'vectorizer': 'text2vec-contextionary',
        "vectorIndexType": "hnsw",
        'properties': [
            {
                'name': 'wikipediaArticleId',
                'description': 'The wikipedia article ID for the book',
                'dataType': ['string'],
                'indexInverted': false // Ignore this property in search and classification
            },
            {
                'name': 'bookTitle',
                'description': 'title of the book',
                'dataType': ['string']
            },
            {
                'name': 'author',
                'description': 'The name of the author',
                'dataType': ['string'],
            },
            {
                'name': 'genres',
                'description': 'Space separated list of the genres of this book',
                'dataType': ['string'],
            },
            {
                'name': 'summary',
                'description': 'Summary of the plot of this book',
                'dataType': ['string'],
            },
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

        for (let i = 0; i < data.length; i++) {
            const obj = data[i];
            console.log(obj)
            await client.data.creator()
                .withClassName('Chapter')
                .withProperties({
                    shortSummary: obj.short_summary,
                    // longSummary: obj.long_summary,
                    chapterNumber: obj.id
                })
                .do()
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
        .withClassName("Book")
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
    const testText = "63 years ago, Linlin's role in Carmel's disappearance caused her to be even more reviled by the giants, and caused a nearby Streusen to take interest in her. Together, Linlin and Streusen formed the beginnings of the Big Mom Pirates, and Linlin's power quickly caused her to become infamous at a young age. Linlin turned the island where the Sheep's House was into Whole Cake Island, where she sought to achieve Carmel's ideals. In the present, the Fire Tank Pirates shoot their KX Launchers at Big Mom, but the power of her scream destroys the shots before they hit her. The Big Mom Pirates then regain their composure, and Caesar attempts to fly in the mirror for the alliance to make a getaway, but Big Mom's scream shatters the mirror. Surrounded by enemies, Bege transforms into a giant fortress and tells his allies to get inside him.";

    const resText = await client.graphql.get()
        .withClassName('Chapter')
        .withFields(['shortSummary', 'chapterNumber'])
        .withNearText({ concepts: [testText] })
        .withLimit(1)
        .do()

    const nearestChapter = resText.data.Get.Chapter[0]
    res.json({
        nearestChapter: nearestChapter
    })
})

router.post("/query-book", async (req, res, next) => {
    const { search, likes, dislikes } = req.body;

    const resText = await client.graphql.get()
        .withClassName('Book')
        .withFields(['bookTitle', 'author', 'genres', 'summary'])
        .withNearText({
            concepts: search,
            moveAwayFrom: {
                concepts: dislikes,
                force: 0.45
            },
            moveTo: {
                concepts: likes,
                force: 0.85
            }
        })
        .withLimit(10)
        .do()

    const nearestBooks = resText.data.Get.Book.map(book => ({
        title: book.bookTitle,
        author: book.title
    }))
    res.json({
        nearestBooks: nearestBooks
    })
})

router.get("/get-schema", async (req, res, next) => {
    const schemaRes = await client.schema.getter().do();
    console.log(schemaRes)
    res.json({
        schema: schemaRes
    })
})

module.exports = router;