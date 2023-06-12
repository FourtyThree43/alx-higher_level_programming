#!/usr/bin/node
// prints a message depending of the number of arguments passed
const args = process.argv.slice(2);
const message = args.length === 0 ? 'No argument' : (args.length === 1 ? 'Argument found' : 'Arguments found');
console.log(message);
