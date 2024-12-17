#!/usr/bin/node
// a script that prints x times “C is fun”
const x = process.argv[2];

if (!parseInt(x)) {
  console.log("Missing number of occurrences");
} else {
  for (let i = 0; i < x; i++) {
    console.log("C is fun");
  }
}
