#!/usr/bin/node
// converts a number from base 10 to another base passed as argument.

exports.converter = (base) => (num) => num.toString(base);
