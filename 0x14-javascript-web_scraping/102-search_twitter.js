#!/usr/bin/node

const request = require('request');
const base64 = require('base-64');
const utf8 = require('utf8');

const hostAuth = 'https://api.twitter.com/oauth2/token';
const cont = `${process.argv[2]}:${process.argv[3]}`;
const contEncoded = base64.encode(utf8.encode(cont));
const searchTweets = 'https://api.twitter.com/1.1/search/tweets.json';

const options = {
  url: hostAuth,
  headers: {
    Authorization: 'Basic ' + utf8.decode(contEncoded),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
  },
  form: {
    grant_type: 'client_credentials'
  }
};

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body).access_token;

    const searchHeads = {
      q: process.argv[4],
      result_type: 'recent',
      count: 5
    };

    const authReqs = {
      url: searchTweets,
      Autorization: 'Bearer ' + info,
      qs: searchHeads
    };

    request.get(authReqs, function (error, response, body) {
      if (!error && response.statusCode === 200) {
        const info2 = JSON.parse(body);
        for (const i in info2.statuses) {
          const stats = `${i.id} ${i.text} by ${i.user.name}`;
          console.log(stats);
        }
      }
    });
  }
}

request.post(options, callback);
