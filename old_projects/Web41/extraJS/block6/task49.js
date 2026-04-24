const prompt = require('prompt-sync')(); 
const number = 12345;

const numberStr = number.toString();
const hasDigit3 = numberStr.includes('3');

const hasDigits2And5 = numberStr.includes('2') && numberStr.includes('5');

console.log(`Число: ${number}`);
console.log(`а) Есть ли в числе цифра 3? ${hasDigit3 ? 'Да' : 'Нет'}`);
console.log(`б) Есть ли в числе цифры 2 и 5? ${hasDigits2And5 ? 'Да' : 'Нет'}`);