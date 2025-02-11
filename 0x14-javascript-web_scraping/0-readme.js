#!/usr/bin/node

// This is a node.js file reader

// fs stands for File system, allowing the script to work with files (r, w, d)
const fs = require("fs");
const filePath = process.argv[2];

// read the file and use callback function to handle errors that may arise
fs.readFile(filePath, "utf-8", (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
