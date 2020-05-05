#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  let msg = '';
  for (let i = 0; i < x; i++) {
    msg += theFunction();
  }
  return (msg);
};
