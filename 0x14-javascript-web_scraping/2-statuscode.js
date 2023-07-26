#!/usr/bin/node
const request = require('request');

const myURL = process.argv[2];
request.get(myURL).on('response', (response) => {
  console.log(`code: ${response.statusCode}`);
});
