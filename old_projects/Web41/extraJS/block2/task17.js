const prompt = require('prompt-sync')();

const num = parseInt(prompt("Введите трехзначное число: "));

if (num < 100 || num > 999) {
    console.log("Ошибка: число должно быть трехзначным.");
} else {

    const numStr = num.toString();


    const newNumStr = numStr.charAt(0) + numStr.charAt(2) + numStr.charAt(1);

    const newNum = parseInt(newNumStr);

    console.log(`Новое число: ${newNum}`);
}