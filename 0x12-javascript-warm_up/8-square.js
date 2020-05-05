#!/usr/bin/node
const times = process.argv[2];
let square;

if (!(Number(times))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < times; i++) {
    square = 'X';
    for (let j = 1; j < times; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
