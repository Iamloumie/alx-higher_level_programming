#!/usr/bin/node
// class that defines a Rectangle added more attributes
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    for (let i = 0; i < this.height; i++) {
      let row = "";
      for (let j = 0; j < this.width; j++) {
        row += "X";
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;
