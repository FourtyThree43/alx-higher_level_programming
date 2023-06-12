#!/usr/bin/node
// searches the second biggest integer in the list of arguments.

const args = process.argv.slice(2).map(Number); // Convert arguments to integers
const numArgs = args.length;

if (numArgs === 0 || numArgs === 1) {
  console.log(0);
} else {
  const max = Math.max(...args);
  const secondMax = Math.max(...args.filter(num => num !== max));

  console.log(secondMax);
}
