#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) throw err;
  if (response.statusCode === 200) {
    const data = {};
    for (const file of JSON.parse(body)) {
      if (file.completed === true) {
        if (file.userId in data) { data[file.userId] += 1; } else { data[file.userId] = 1; }
      }
    }
    console.log(data);
  }
});
