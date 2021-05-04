#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const data = process.argv[2];
request(url + data, function (err, response, body) {
  if (response.statusCode === 200) {
    const filejson = JSON.parse(body);
    console.log(filejson.title);
  } else if (err) {
    return console.log(err);
  }
});
