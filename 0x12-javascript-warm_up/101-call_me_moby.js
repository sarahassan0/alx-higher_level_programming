#!/usr/bin/node
const callMeMoby = (x, theFunction) => {
  while (x--) theFunction();
};
exports.callMeMoby = callMeMoby;
