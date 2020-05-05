#!/usr/bin/node
const x = process.argv[2];

if (!(Number(x))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
