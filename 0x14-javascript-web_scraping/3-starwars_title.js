#!/usr/bin/node
// A script that prints the title of a star wars movies where
// the episode number matches a given integer
// process.argv[2] gets the star war movie episode number
const request = require("request");
const episode_no = process.argv[2];
const url = "https://swapi-api.alx-tools.com/api/films/" + episode_no;
// get the body and parse out what is needed
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
