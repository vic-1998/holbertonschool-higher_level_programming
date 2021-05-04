#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const data = process.argv[3];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(data, body, 'utf-8', function (err, file) {
      if (err != null) {
        console.log(err);
      }
    });
  }
});
