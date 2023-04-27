#!/usr/bin/node

const request = require('request');

const movie_id = process.argv[2]

const API = `https://swapi-api.alx-tools.com/api/films/${movie_id}`

const options = {
  url: API,
  json: true
};

request(options, (error, response, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data.title);
  }
});
