#!/usr/bin/node

const request = require('request');

const options = {
  url: `${process.argv[2]}`,
  headers: {
    'User-Agent': 'request'
  }
};

let count = 0;
function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body);
    for (const i in info.results) {
      const allChars = info.results[i].characters;
      allChars.forEach(cha => {
        if (cha.includes('/18/')) {
          count++;
        }
      });
    }
    console.log(count);
  }
}

request(options, callback);
