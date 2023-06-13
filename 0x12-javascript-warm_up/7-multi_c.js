#!/usr/bin/node
// prints x times “C is fun”
const args = process.argv.slice(2);
const x = parseInt(args[0], 10); // number of occurrences

if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
