#!/usr/bin/node

const myVar = process.argv[2];

if (Number(myVar)) {
  console.log('My number: ' + parseInt(myVar));
} else {
  console.log('Not a number');
}
