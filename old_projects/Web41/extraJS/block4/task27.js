const prompt = require('prompt-sync')();

function isPalindrome(number) {
    if (number < 100 || number > 999) {
        console.log("Пожалуйста, введите трехзначное число.");
        return;
    }
    let strNumber = number.toString();
    if (strNumber === strNumber.split('').reverse().join('')) {
        console.log(`${number} является палиндромом.`);
    } else {
        console.log(`${number} не является палиндромом.`);
    }
}
let number = parseInt(prompt("Введите трехзначное число:"));
if (!isNaN(number)) {
    isPalindrome(number);
} else {
    console.log("Пожалуйста, введите корректное число.");
}