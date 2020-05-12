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
    for (let i in info.results) {
      const all_chars = info.results[i].characters;
      const chart = "https://swapi-api.hbtn.io/api/people/18/";
      if (all_chars.includes(chart)) {
        count++;
      }
    }
    console.log(count);
  }
}

request(options, callback);
