#!/usr/bin/node
// function that returns the number of occurences in a list

exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
