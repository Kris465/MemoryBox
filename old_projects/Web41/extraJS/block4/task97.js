const prompt = require('prompt-sync')();

function findNumbers(a, b, c) {
    let largest, smallest, middle;

    if (a > b && a > c) {
        largest = a;
    } else if (b > a && b > c) {
        largest = b;
    } else {
        largest = c;
    }

    if (a < b && a < c) {
        smallest = a;
    } else if (b < a && b < c) {
        smallest = b;
    } else {
        smallest = c;
    }

    if ((a > smallest && a < largest)) {
        middle = a;
    } else if ((b > smallest && b < largest)) {
        middle = b;
    } else {
        middle = c;
    }

    return {
        largest: largest,
        smallest: smallest,
        middle: middle
    };
}

const num1 = parseInt(prompt("Введите первое целое число:"));
const num2 = parseInt(prompt("Введите второе целое число:"));
const num3 = parseInt(prompt("Введите третье целое число:"));

if (num1 === num2 || num1 === num3 || num2 === num3) {
    console.log("Числа должны быть различными.");
} else {
    const result = findNumbers(num1, num2, num3);
    
    console.log(`Наибольшее число: ${result.largest}`);
    console.log(`Наименьшее число: ${result.smallest}`);
    console.log(`Среднее число: ${result.middle}`);
}