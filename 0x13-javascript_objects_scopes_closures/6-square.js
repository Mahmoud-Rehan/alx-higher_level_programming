#!/usr/bin/node

const Mysquare = require('./5-square');

class Square extends Mysquare {
  charPrint (c) {
    if (c === undefined) {
      this.print(c);
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write(c);
        }
        console.log('');
      }
    }
  }
}

module.exports = Square;
