#!/usr/bin/node
// script that prints a square
const x = process.argv[2];

if (!parseInt(x)) {
  console.log("Missing size");
} else {
  for (let i = 0; i < x; i++) {
    let row = "";
    for (let j = 0; j < x; j++) {
      row += "X";
    }
    console.log(row);
  }
}
