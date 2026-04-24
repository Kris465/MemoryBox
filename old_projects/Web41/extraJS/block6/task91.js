const prompt = require('prompt-sync')(); 

function analyzeNumber(num) {
  const numStr = num.toString();
  const digits = numStr.split('').map(Number);
  const length = digits.length;

  const digitCount = length;

  const sum = digits.reduce((acc, digit) => acc + digit, 0);

  const product = digits.reduce((acc, digit) => acc * digit, 1);

  const average = sum / digitCount;

  const sumOfSquares = digits.reduce((acc, digit) => acc + digit ** 2, 0);

  const sumOfCubes = digits.reduce((acc, digit) => acc + digit ** 3, 0);

  const firstDigit = digits[0];

  const sumFirstLast = firstDigit + digits[length - 1];

  return {
    digitCount,      
    sum,             
    product,         
    average,         
    sumOfSquares,    
    sumOfCubes,      
    firstDigit,      
    sumFirstLast     
  };
}

const number = 1234;
const result = analyzeNumber(number);

console.log(`Число: ${number}`);
console.log(`а) Количество цифр: ${result.digitCount}`);
console.log(`б) Сумма цифр: ${result.sum}`);
console.log(`в) Произведение цифр: ${result.product}`);
console.log(`г) Среднее арифметическое: ${result.average}`);
console.log(`д) Сумма квадратов цифр: ${result.sumOfSquares}`);
console.log(`е) Сумма кубов цифр: ${result.sumOfCubes}`);
console.log(`ж) Первая цифра: ${result.firstDigit}`);
console.log(`з) Сумма первой и последней цифры: ${result.sumFirstLast}`);