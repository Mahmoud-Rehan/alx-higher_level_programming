#!/usr/bin/node

exports.converter = function (base) {
  function converting (num) {
    return num.toString(base);
  }

  return converting;
};
