#!/usr/bin/node
const request = require('request');
const data = process.argv[2];
request(data, function (err, response) {
  if (err) {
    return console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
