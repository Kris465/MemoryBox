const prompt = require('prompt-sync')();

const num = parseInt(prompt("Введите двузначное число: "));

if (num < 10 || num > 99) {
    console.log("Ошибка: число должно быть двузначным.");
} else {
    const tens = Math.floor(num / 10);
    const units = num % 10;       
    const result =units * 10 + tens;
    console.log(`Число, образованное при перестановке цифр заданного числа: ${result}`)
}