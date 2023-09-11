#!/usr/bin/node
const callMeMoby = function (x, theFunction) {
  while (x) {
    theFunction();
    x--;
  }
};
exports.callMeMoby = callMeMoby;
