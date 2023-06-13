#!/usr/bin/node
const Square = require('./6-square');

const s1 = new Square(4);
console.log('+-----undefined:------+');
s1.charPrint();
console.log('+-----defined:------+');
s1.charPrint('C');
console.log('+-----defined:------+');
s1.charPrint('W');
