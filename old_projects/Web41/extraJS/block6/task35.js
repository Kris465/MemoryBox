const prompt = require('prompt-sync')();

const result = [];
let num = 500;
while (result.length < 20) {
  if (num % 13 === 0 || num % 17 === 0) {
    result.push(num);
  }
  num++;
}
console.log(result);