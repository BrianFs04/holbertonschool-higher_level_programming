#!/usr/bin/node
let myVar;

if (myVar === process.argv[2]) {
    console.log('No argument');
} else if (myVar === process.argv[3]) {
    console.log('Argument found');
} else {
    console.log('Arguments found')
}
