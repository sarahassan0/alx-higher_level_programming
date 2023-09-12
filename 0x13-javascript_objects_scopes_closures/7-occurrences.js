#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = list.length;
  let occur = 0;
  while (i--) {
    if (list[i] === searchElement) occur++;
  }
  return occur;
};
