#!/usr/bin/node

// This is a node.js file writing

// process.argv is an array containg command line arguments
// 		process.argv[0] is the path to node.js (/usr/bin/node)
// 		process.argv[1] is the path to the script
// 		process.argv[2] is the first usr-provided argument (file path)
// 		process.argv[3] is second user-provided arg (content to write in  file)

const fs = require("fs");
const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, "utf-8", (error) => {
  if (error) {
    console.error(error);
  }
});
