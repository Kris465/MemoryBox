const prompt = require('prompt-sync')(); 
const numberStr = prompt("Введите натуральное число:");


function findEightsFromEnd(numberStr) {
  const digits = numberStr.split('');

  for (let i = digits.length - 1; i >= 0; i--) {
    if (digits[i] === '8') {
   
      return digits.length - i;
    }
  }

  return 0;
}

const position = findEightsFromEnd(numberStr);
console.log(position);