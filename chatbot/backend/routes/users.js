const fs = require("fs");
var express = require('express');
var router = express.Router();

router.get('/get-profile', (req, res, _next) => {
  const { name } = req.query;

  const filePath = './data/users.json'
  let data = fs.readFileSync(filePath, 'utf8')
  data = JSON.parse(data);

  if (data[name]) {
    res.status(200).json(data[name])
  } else { // new user
    data[name] = {
      likes: "",
      dislikes: ""
    }

    let json = JSON.stringify(data)
    fs.writeFileSync(filePath, json, 'utf8');

    res.status(200).json(data[name])
  }
})

router.post('/set-profile', (req, res, _next) => {
  const { name, likes, dislikes } = req.body;

  const filePath = './data/users.json'
  let data = fs.readFileSync(filePath, 'utf8')
  data = JSON.parse(data)

  data[name] = {
    likes: likes,
    dislikes: dislikes
  }

  const json = JSON.stringify(data);
  fs.writeFileSync(filePath, json, 'utf8')

  res.status(200).send('User modified');
})

module.exports = router;
