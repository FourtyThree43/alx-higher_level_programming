#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const moviesData = JSON.parse(body).results;
    const moviesWithCharacter = moviesData.reduce((count, movie) => {
      return movie.characters.find((characterUrl) => characterUrl.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0);
    console.log(moviesWithCharacter);
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
