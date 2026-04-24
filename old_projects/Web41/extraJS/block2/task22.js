const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите натуральное число (n > 99): "));

if (n <= 99) {
    console.log("Ошибка: число должно быть больше 99.");
} else {
    const tens = Math.floor((n % 100) / 10);

    const hundreds = Math.floor(n / 100) % 10;

    console.log(`Число десятков: ${tens}`);
    console.log(`Число сотен: ${hundreds}`);
}