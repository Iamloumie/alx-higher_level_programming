#!/usr/bin/node
// function that converts a number from base 10 to another base

exports.converter = function (base) {
  function myConverter(n) {
    return n.toString(base);
  }

  return myConverter;
};
