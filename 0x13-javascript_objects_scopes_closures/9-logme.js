#!/usr/bin/node
// function that prints the number of arguments and argument values

let counter = 0;
exports.logMe = function (item) {
  counter++;
  console.log(`${counter - 1}: ${item}`);
};
