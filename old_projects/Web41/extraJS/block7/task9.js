const prompt = require('prompt-sync')();

console.log("а) Двухзначные числа, сумма квадратов цифр которых делится на 13:");

for (let num = 10; num <= 99; num++) {
    const tens = Math.floor(num / 10);
    const units = num % 10;
    const sumSquares = tens * tens + units * units;

    if (sumSquares % 13 === 0) {
        console.log(num);
    }
}

console.log("б) Двухзначные числа с свойством: сумма цифр + (сумма цифр)^2 = число");

for (let num = 10; num <= 99; num++) {
    const tens = Math.floor(num / 10);
    const units = num % 10;
    const sumDigits = tens + units;
    const result = sumDigits + sumDigits * sumDigits;

    if (result === num) {
        console.log(num);
    }
}