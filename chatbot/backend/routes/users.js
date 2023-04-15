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
      likedBooks: [""],
      dislikedBooks: [""],
      likedGenres: [""],
      dislikedGenres: [""]
    }

    let json = JSON.stringify(data)
    fs.writeFileSync(filePath, json, 'utf8');

    res.status(200).json(data[name])
  }
})

module.exports = router;
