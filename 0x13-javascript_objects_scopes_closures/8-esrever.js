#!/usr/bin/node
exports.esrever = function (list) {
  const x = [];
  for (let i = 0; i < list.length; i++) {
    x.unshift(list[i]);
  }
  return x;
};
