const prompt = require('prompt-sync')();

function sumOfTwoLargest(a, b, c) {
    let largest, secondLargest;

    if (a > b && a > c) {
        largest = a;
        secondLargest = Math.max(b, c);
    } else if (b > a && b > c) {
        largest = b;
        secondLargest = Math.max(a, c);
    } else {
        largest = c;
        secondLargest = Math.max(a, b);
    }
    return largest + secondLargest;
}

const num1 = parseFloat(prompt("Введите первое число:"));
const num2 = parseFloat(prompt("Введите второе число:"));
const num3 = parseFloat(prompt("Введите третье число:"));


if (num1 === num2 || num1 === num3 || num2 === num3) {
    console.log("Числа должны быть различными.");
} else {
    const sum = sumOfTwoLargest(num1, num2, num3);
    
    console.log(`Сумма двух наибольших чисел: ${sum}`);
}