const prompt = require('prompt-sync')();

const num = parseInt(prompt("Введите трехзначное число: "));

if (num < 100 || num > 999) {
    console.log("Ошибка: число должно быть трехзначным.");
} else {

    const reversedNum = parseInt(num.toString().split('').reverse().join(''));
    
    console.log(`Число, полученное при прочтении цифр справа налево: ${reversedNum}`);
}
