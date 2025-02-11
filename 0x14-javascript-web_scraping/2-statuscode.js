#!/usr/bin/node

// A script that displays the status code of a GET request

const request = require("request");
const urlToMakeReq = process.argv[2];

request(urlToMakeReq, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("code:", response.statusCode);
  }
});
