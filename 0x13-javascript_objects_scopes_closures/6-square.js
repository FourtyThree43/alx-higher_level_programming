#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle
const SquareParent = require('./5-square');

class Square extends SquareParent {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
