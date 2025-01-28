const prompt = require('prompt-sync')(); 

const n = prompt('Передайте число: ');

function fibonacci(n) {
    if (n <= 0) {
        return "Порядковый номер должен быть положительным.";
    } else if (n === 1 || n === 2) {
        return 1;
    }

    let a = 1, b = 1;
    for (let i = 3; i <= n; i++) {
        let temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

console.log(`Число Фибоначчи по переданному порядковому номеру: ${fibonacci(n)}`);