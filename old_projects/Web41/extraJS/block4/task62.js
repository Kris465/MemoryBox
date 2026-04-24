const prompt = require('prompt-sync')();


function hasExactlyThreeSameDigits(n) {

    const numberStr = n.toString().padStart(4, '0');

    const digitCount = {};

    for (let digit of numberStr) {
        digitCount[digit] = (digitCount[digit] || 0) + 1;
    }


    return Object.values(digitCount).includes(3);
}


const input = prompt("Введите натуральное число (n <= 9999):");
const n = parseInt(input);


if (isNaN(n) || n < 0 || n > 9999) {
    console.log("Пожалуйста, введите корректное натуральное число от 0 до 9999.");
} else {
    const result = hasExactlyThreeSameDigits(n);
    console.log(`Число ${n} ${result ? "содержит" : "не содержит"} ровно три одинаковые цифры.`);
}