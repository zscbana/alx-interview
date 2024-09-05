#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(apiUrl, (error, response, body) => {
  if (error) throw error;
  
  const characterUrls = JSON.parse(body).characters;
  fetchCharactersInOrder(characterUrls, 0);
});

const fetchCharactersInOrder = (characterUrls, index) => {
  if (index === characterUrls.length) return;

  request(characterUrls[index], (error, response, body) => {
    if (error) throw error;

    console.log(JSON.parse(body).name);
    fetchCharactersInOrder(characterUrls, index + 1);
  });
};
