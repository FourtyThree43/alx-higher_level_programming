#!/usr/bin/node
const esrever = require('./8-esrever').esrever;

console.log('+--------------+list:+--------------+');

console.log([1, 2, 3, 4, 5]);
console.log(['School', 89, { id: 12 }, 'String']);

console.log('+--------------+reversed:+--------------+');

console.log(esrever([1, 2, 3, 4, 5]));
console.log(esrever(['School', 89, { id: 12 }, 'String']));
