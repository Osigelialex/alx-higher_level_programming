#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const API = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

const options = {
  url: API,
  json: true
};

request(options, (error, response, data) => {
  if (error) {
    console.error(error);
  } else {
    data.characters.forEach((link) => {
      request({ url: link, json: true }, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const name = body.name;
          console.log(name);
        }
      });
    });
  }
});
