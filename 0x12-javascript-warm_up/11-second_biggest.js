#!/usr/bin/node
'use strict';
let x = 0;
let arg = process.argv.slice(2);
if (arg.length > 1) {
  arg.sort();
  x = arg[arg.length - 2];
}
console.log(x);
