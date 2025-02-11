#!/usr/bin/node

// a script that prints all characters of a Star Wars movie:
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name by line
// Using the Star wars API and the module request

const request = require("request");

if (process.argv.length < 3) {
  console.log("Usage: ./starwars_characters.js <movie_id>");
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Can't fetch (status code: ${response.statusCode})`);
    return;
  }

  const filmData = JSON.parse(body);
  filmData.characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        return;
      }
      if (charResponse.statusCode === 200) {
        console.log(JSON.parse(charBody).name);
      }
    });
  });
});
