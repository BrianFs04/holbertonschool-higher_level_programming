#!/usr/bin/node
let myVar;

if (myVar === process.argv[2]) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
