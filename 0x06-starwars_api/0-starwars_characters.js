#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const options = {
  url: `https://swapi.dev/api/films/${movieId}/`,
  method: 'GET',
  headers: {
    'User-Agent': 'request',
  },
};

request(options, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    const characters = film.characters;

    characters.forEach((characterUrl) => {
      request({ url: characterUrl, method: 'GET', headers: { 'User-Agent': 'request' } }, (err, resp, charBody) => {
        if (!err && resp.statusCode === 200) {
          const character = JSON.parse(charBody);
          console.log(character.name);
        }
      });
    });
  }
});

