#!/usr/bin/node

const list = require('./100-data.js').list;
const ops = list.map(function (num, index) {
  return num * index;
});
console.log(list);
console.log(ops);
