const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите натуральное число (n > 9): "));

if (n <= 9) {
    console.log("Ошибка: число должно быть больше 9.");
} else {
    const units = n % 10;
    const tens = Math.floor((n % 100) / 10);

    console.log(`Число единиц: ${units}`);
    console.log(`Число десятков: ${tens}`);
}