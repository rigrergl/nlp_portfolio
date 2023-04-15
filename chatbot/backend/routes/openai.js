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

module.exports = router;