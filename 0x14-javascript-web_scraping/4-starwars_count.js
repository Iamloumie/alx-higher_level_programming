#!/usr/bin/node

// This script sends a request to a website (an API) to get information
// about Star Wars movies. Then, it counts how many times a specific
// character (with "18" in their ID) appears in all the movies and
// prints that number.

const request = require("request");
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const jsonData = JSON.parse(body).results; // extracting data
    let count = 0;

    for (let i = 0; i < jsonData.length; i++) {
      const characters = jsonData[i].characters; // list of movie characters

      // checking each character in the movie
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes("18")) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
