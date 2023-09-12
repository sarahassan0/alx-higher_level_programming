#!/usr/bin/node
exports.esrever = function (list, searchElement) {
  let i = list.length;
  const arr = [];
  while (i--) {
    arr.push(list[i]);
  }
  return arr;
};
