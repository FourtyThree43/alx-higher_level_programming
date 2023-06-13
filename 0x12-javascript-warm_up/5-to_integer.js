#!/usr/bin/node
// prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer.
const args = process.argv.slice(2);
const toInt = parseInt(args[0], 10);

if (!isNaN(toInt)) {
  console.log(`My number: ${toInt}`);
} else {
  console.log('Not a number');
}
