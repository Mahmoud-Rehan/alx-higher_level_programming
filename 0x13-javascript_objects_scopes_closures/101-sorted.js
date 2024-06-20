#!/usr/bin/node

const list = require('./101-data').dict;
const sortDict = {};

Object.keys(list).forEach(key => {
  if (sortDict[list[key]] === undefined) {
    sortDict[list[key]] = [];
  }

  sortDict[list[key]].push(key);
});

console.log(sortDict);
