const prompt = require('prompt-sync')();

function skleivChisel(num1, num2, num3) {
    const result = String(num1) + String(num2) + String(num3);
    const result1 = Number(result);
    return result1;
}

let num1 = parseInt(prompt('введите первое число: '));
let num2 = parseInt(prompt('введите второе число: '));
let num3 = parseInt(prompt('введите третье число: '));

const result = skleivChisel(num1, num2, num3);
console.log(`цифра ${result}`);