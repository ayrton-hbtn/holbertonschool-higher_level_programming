#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const url = 'https://swapi-api.hbtn.io/api/films';

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const movie = JSON.parse(body).results[argv[2] - 1];
  const characters = movie.characters;
  for (const char of characters) {
    console.log(char);
    request(char, (err, res, body) => {
      if (err) {
        console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
