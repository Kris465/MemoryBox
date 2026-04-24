const prompt = require('prompt-sync')();

const numberStr = prompt("Введите натуральное число:");


function countMaxDigitOccurrences(numberStr) {
  const digits = numberStr.split('');
  const maxDigit = Math.max(...digits.map(Number));
  let count = 0;

  for (let digit of digits) {
    if (Number(digit) === maxDigit) {
      count++;
    }
  }

  return count;
}

const result = countMaxDigitOccurrences(numberStr);
console.log(result);