#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const myURL = process.argv[2];
const filePath = process.argv[3];

request.get(myURL, (getErr, response, body) => {
  if (getErr) {
    console.error(getErr);
  } else if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf-8', (writeErr) => {
      if (writeErr) console.error(writeErr);
    });
  } else {
    console.log(`Error code: ${response.statusCode}`);
  }
});
