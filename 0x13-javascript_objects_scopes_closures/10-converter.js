#!/usr/bin/node

exports.converter = function (base) {
  return function (toBase) {
    return toBase.toString(base);
  };
};
