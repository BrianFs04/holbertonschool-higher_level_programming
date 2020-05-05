#!/usr/bin/node

const myVar = [];

if (!(process.argv[2]) || !(process.argv[3])) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    myVar.push(process.argv[i]);
  }
  myVar.sort().pop();
  console.log(parseInt(myVar.slice(-1)));
}
