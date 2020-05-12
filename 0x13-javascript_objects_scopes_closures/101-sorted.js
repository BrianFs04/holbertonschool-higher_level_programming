#!/usr/bin/node

const dict = require('./101-data.js').dict;

const nums = Object.keys(dict).reduce((acc, k) => {
  const num = dict[k];
  acc[num] = acc[num] || [];
  acc[num].push(k);
  return acc;
}, {});

console.log(nums);
