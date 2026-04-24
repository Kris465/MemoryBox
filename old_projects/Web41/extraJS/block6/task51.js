const prompt = require('prompt-sync')(); 

const numberInput = prompt("Введите натуральное число:");
const number = parseInt(numberInput, 10);

if (isNaN(number) || number <= 0) {
    console.log("Некорректный ввод");
} else {
    const strNumber = number.toString();
    const reversedStr = strNumber.split('').reverse().join('');
    const isPalindrome = strNumber === reversedStr;
    console.log(`Число ${number} ${isPalindrome ? 'является' : 'не является'} палиндромом`);
}