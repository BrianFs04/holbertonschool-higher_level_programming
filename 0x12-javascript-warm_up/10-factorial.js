#!/usr/bin/node

const num = parseInt(process.argv[2]);

function factorial (val) {
  if (val === 0) {
    return (1);
  } else if (!(process.argv[2])) {
    return (1);
  }
  return (val * factorial(val - 1));
}
console.log(factorial(num));
