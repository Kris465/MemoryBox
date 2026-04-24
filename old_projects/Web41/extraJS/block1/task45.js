const prompt = require('prompt-sync')();

function pepesi(num1, num2) {
    const sum = num1 + num2;
    const difference = num1 - num2;
    const product = num1 * num2;
    const quotient = num2 !== 0 ? num1 / num2 : 'Деление на ноль невозможно';
    
    return { sum, difference, product, quotient };
}
const num1 = prompt("Введите первое число:");
const num2 = prompt("Введите второе число:");

const result = pepesi(num1, num2);

console.log(`Сумма: ${result.sum}`);
console.log(`Разность: ${result.difference}`);
console.log(`Произведение: ${result.product}`);
console.log(`Частное: ${result.quotient}`);