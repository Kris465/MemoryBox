const prompt = require('prompt-sync')();

let k = parseInt(prompt("Введите значение k (1 <= k <= 150): "));

if (k < 1 || k > 150) {
    console.log("k должно быть в диапазоне от 1 до 150.");
} else {
    let threeDigitNumbers = '';
    for (let i = 101; i <= 150; i++) {
        threeDigitNumbers += i.toString();
    }

    let digit = threeDigitNumbers[k - 1];

    console.log(`k-я цифра: ${digit}`);

    if (k % 3 === 0) {
        console.log(`k - кратное трём: ${digit}`);
    }

    if ((k - 1) % 3 === 0) {
        console.log(`k - одно из чисел 1, 4, 7, ...: ${digit}`);
    }

    if ((k - 2) % 3 === 0) {
        console.log(`k - одно из чисел 2, 5, 8, ...: ${digit}`);
    }
}