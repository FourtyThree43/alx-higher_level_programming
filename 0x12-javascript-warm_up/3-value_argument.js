#!/usr/bin/node
// prints the first argument passed to it.
const args = process.argv.slice(2);
const hasArgs = Boolean(args[0]);

console.log(hasArgs ? args.join('\n') : 'No argument');
