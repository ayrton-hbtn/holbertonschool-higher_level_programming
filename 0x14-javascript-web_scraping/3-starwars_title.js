#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
