#!/usr/bin/node

const request = require('request');

const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/',
  headers: {
    'User-Agent': 'request'
  }
};

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body);
    for (const i in info.characters) {
      request(info.characters[i], function (error, respose, body) {
        if (!error && response.statusCode === 200) {
          const chars = JSON.parse(body);
          console.log(chars.name);
        }
      });
    }
  }
}

request(options, callback);
