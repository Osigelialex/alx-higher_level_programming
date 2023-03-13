#!/usr/bin/node

const process = require('process');
const value = process.argv[2];

if (isNaN(value)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < value; i++) {
    console.log('X'.repeat(value));
  }
}
