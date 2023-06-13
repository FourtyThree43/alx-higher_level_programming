#!/usr/bin/node
// prints the addition of 2 integers

function add (a, b) {
  return (a + b);
}

const args = process.argv.slice(2);
const arg1 = parseInt(args[0], 10);
const arg2 = parseInt(args[1], 10);

console.log(add(arg1, arg2));
