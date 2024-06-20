#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let num = 0;

  while (list[i]) {
    if (list[i] === searchElement) {
      num++;
    }
    i++;
  }
  return (num);
};
