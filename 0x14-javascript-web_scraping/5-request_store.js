#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.
const request = require("request");
const fs = require("fs");
const url = process.argv[2];
const filePathBodyRes = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePathBodyRes, body, "utf-8", (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
