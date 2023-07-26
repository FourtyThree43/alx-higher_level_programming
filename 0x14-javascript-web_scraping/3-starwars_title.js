#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];
const apiURL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(apiURL, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  } else {
    console.log(`Error code: ${response.statusCode}`);
  }
});
