#!/usr/bin/node

const request = require('request');

const options = {
  url: `${process.argv[2]}`,
  headers: {
    'User-Agent': 'request'
  }
};

const idList = [];
const idDict = {};
function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body);
    for (const i in info) {
      if (info[i].completed === true) {
        idList.push(info[i].userId);
      }
    }
    idList.forEach(function (i) { idDict[i] = (idDict[i] || 0) + 1; });
    console.log(idDict);
  }
}

request(options, callback);
