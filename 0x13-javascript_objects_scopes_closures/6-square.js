#!/usr/bin/node
// class that defines a square that inherits from 5-square.js

const Square1 = require("./5-square.js");

class Square extends Square1 {
  charprint(c) {
    if (c === undefined) {
      c = "X";
    }
    for (let i = 0; i < this.height; i++) {
      let row = "";
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
