#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const options = {
  url: `${process.argv[2]}`,
  headers: {
    'User-Agent': 'request'
  }
};

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    fs.writeFileSync(process.argv[3], body, 'utf8');
  }
}

request(options, callback);
