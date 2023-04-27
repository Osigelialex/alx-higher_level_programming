#!/usr/bin/node

const request = require('request');

const PATH = process.argv[2];
request(PATH, (error, response, body) => {
  console.log('code:', response && response.statusCode);
});
