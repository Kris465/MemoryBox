const prompt = require('prompt-sync')();

const numberStr = prompt("Введите натуральное число:");

function countMinDigitOccurrences(numberStr) {
  const digits = numberStr.split('');
  const minDigit = Math.min(...digits.map(Number));
  let count = 0;

  for (let digit of digits) {
    if (Number(digit) === minDigit) {
      count++;
    }
  }

  return count;
}

const result = countMinDigitOccurrences(numberStr);
console.log(result);