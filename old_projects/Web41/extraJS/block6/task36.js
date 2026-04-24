const prompt = require('prompt-sync')();

const result = [];
let num = 100;
while (result.length < 10) {
  if (num % 9 === 0 && num % 10 === 7) {
    result.push(num);
  }
  num++;
}
console.log(result);