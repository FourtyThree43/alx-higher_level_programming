#!/usr/bin/node
// computes and prints a factorial

function factorial (n) {
  return ((n === 0 || n === 1) ? 1 : n * factorial(n - 1));
}

const args = process.argv.slice(2);
const arg1 = parseInt(args[0], 10);
const result = (isNaN(arg1)) ? 1 : factorial(arg1);

console.log(result);
