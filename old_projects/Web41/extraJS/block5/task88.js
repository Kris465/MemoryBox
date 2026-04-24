const prompt = require('prompt-sync')();
function cubeUsingOddNumbers(n) {
    let sum = 0;
    let oddNumber = 1;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            sum += oddNumber;
            oddNumber += 2;
        }
    }

    return sum;
}

const userInput = prompt("Введите натуральное число n:");
const n = parseInt(userInput);

if (!isNaN(n) && n > 0) {
    const result = cubeUsingOddNumbers(n);
    console.log(`Куб числа ${n} равен ${result}`);
} else {
    console.log("Пожалуйста, введите корректное натуральное число.");
}