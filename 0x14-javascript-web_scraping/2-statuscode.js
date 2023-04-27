#!/usr/bin/node

const request = require('request');

const PATH = process.argv[2];
request(PATH, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response && response.statusCode);
  }
});
