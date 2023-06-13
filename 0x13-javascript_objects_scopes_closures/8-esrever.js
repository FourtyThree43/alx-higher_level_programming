#!/usr/bin/node
//  Returns the reversed version of a list withou using reverse().

exports.esrever = function (list) {
  let start = 0;
  let end = list.length - 1;

  while (start < end) {
    [list[start], list[end]] = [list[end], list[start]];
    start++;
    end--;
  }

  return list;
};
