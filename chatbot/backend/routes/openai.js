var express = require('express');
var router = express.Router();

const { Configuration, OpenAIApi } = require("openai");

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

router.get("/", (req, res, next) => {
    res.send('hello world')
})

router.get("/completion", async (req, res, next) => {
    chatRes = await openai.createChatCompletion({
        model: "gpt-3.5-turbo",
        messages: [{role: "user", content: "Hello ChatGPT"}]
    })

    console.log(chatRes)
    console.log()
    console.log(chatRes.data.choices)

    res.status(200)
})

router.post("/extract-name", async (req, res, _next) => {
    const { userInput } = req.body

    chatRes = await openai.createChatCompletion({
        model: "gpt-3.5-turbo",
        messages: [{role: "user", content: `Extract the user's name from the following message: "${userInput}"
        Answer only with the user's name.
        
        User name: `}]
    })

    let name = chatRes.data.choices[0].message.content;
    name = name.toLowerCase()
   
    res.status(200).json({
        name: name
    })
})

router.post("/extract-preference-list", async (req, res, _next) => {
    const { userInput } = req.body;

    chatRes = await openai.createChatCompletion({
        model: "gpt-3.5-turbo",
        messages: [{role: "user", content: `Can you cleanup the user's preferences to be a comma-separated list of values:
        "${userInput}"
        
        output only the comma separated list and nothing else. No commas
        For example,  for "I dislike romance  and comedy, as well as mystery" you output should be:
        List: Romance, comedy, mystery
        
        List: `}]
    })

    const preferences = chatRes.data.choices[0].message.content;

    res.status(200).json({
        preferences: preferences
    })
})

router.post("/clean-search", async (req, res, _next) => {
    const { userInput } = req.body;

    chatRes = await openai.createChatCompletion({
        model: "gpt-3.5-turbo",
        messages: [{role: "user", content: `can you clean the following user input, which is their answer to what they are looking for in a book. I need the user input to be cleaned up to get the best results when I put it as a query to a vector database containing plot summaries of many different books.
        Please output the query and nothing else. Please separate concepts using commas.
        
        Raw user input:
        "${userInput}"
        
        Query:`}]
    });

    const cleanSearch = chatRes.data.choices[0].message.content;

    res.status(200).json({
        cleanSearch: cleanSearch
    })
})

router.post("/get-yes-no", async (req, res, _next) => {
    const { userInput } = req.body;

    chatRes = await openai.createChatCompletion({
        model: "gpt-3.5-turbo",
        messages: [{role: "user", content: `can you evaluate the following user input as rather a "Yes" or "No". Your output should be only one word and nothing else. Please do not include any punctuation.

        Raw user input:
        "${userInput}"
        
        Yes or No:`}]
    });

    const isYes = chatRes.data.choices[0].message.content.toLowerCase() === "yes";

    res.status(200).json({
        isYes: isYes
    })
})

module.exports = router;