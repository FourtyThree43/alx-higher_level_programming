#!/usr/bin/node
// prints two arguments passed to it, in the following format: “ is ”.
const args = process.argv.slice(2);
const arg1 = args[0];
const arg2 = args[1];

console.log(`${arg1} is ${arg2}`);
