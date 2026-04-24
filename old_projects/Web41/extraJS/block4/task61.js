const prompt = require('prompt-sync')();

function isPalindrome(n) {

    const numberStr = n.toString().padStart(4, '0');

   
    const reversedStr = numberStr.split('').reverse().join('');
    return numberStr === reversedStr;
}

const input = prompt("Введите натуральное число (n <= 9999):");
const n = parseInt(input);


if (isNaN(n) || n < 0 || n > 9999) {
    console.log("Пожалуйста, введите корректное натуральное число от 0 до 9999.");
} else {
 
    const result = isPalindrome(n);
    console.log(`Число ${n} ${result ? "является" : "не является"} палиндромом.`);
}