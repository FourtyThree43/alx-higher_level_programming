#!/usr/bin/node
const request = require('request');

function fetchMovieCharacters (movieID) {
  const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieID}/`;

  request.get(apiUrl, (err, response, body) => {
    if (err) {
      console.error(err);
    } else if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const charData = movieData.characters;
      fetchCharactersRecursively(charData, 0);
    } else {
      console.log(`Error code: ${response.statusCode}`);
    }
  });
}

function fetchCharactersRecursively (charData, index) {
  if (index >= charData.length) {
    return; // Stop when all characters have been printed
  }

  const characterUrl = charData[index];

  request.get(characterUrl, (err, response, body) => {
    if (err) {
      console.error(err);
    } else if (response.statusCode === 200) {
      const character = JSON.parse(body);
      console.log(character.name);
      fetchCharactersRecursively(charData, index + 1); // Fetch the next character
    } else {
      console.log(`Error code: ${response.statusCode}`);
      fetchCharactersRecursively(charData, index + 1); // Fetch the next character even if there's an error
    }
  });
}

const movieID = process.argv[2];
if (!movieID) {
  console.log('Please provide a movie ID as the first argument.');
} else {
  fetchMovieCharacters(movieID);
}
