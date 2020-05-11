#!/usr/bin/node
const Squarel = require('./5-square.js');

module.exports = class Square extends Squarel {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      if (c === undefined) {
        console.log('X'.repeat(this.width));
      } else {
        console.log('C'.repeat(this.width));
      }
    }
  }
};
