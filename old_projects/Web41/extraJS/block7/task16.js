const prompt = require('prompt-sync')();

const numbers = [];
for (let i = 1; i <= 10; i++) {
    const input = prompt(`Введите число ${i}:`);
    const num = parseInt(input, 10);
    if (!isNaN(num)) {
        numbers.push(num);
    } else {
        alert("Некорректный ввод. Пожалуйста, введите число.");
        i--; 
    }
}

const sumEven = numbers.reduce((sum, num) => (num % 2 === 0 ? sum + num : sum), 0);

console.log("Сумма четных чисел:", sumEven);