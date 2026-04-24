const prompt = require('prompt-sync')();
function sumOfCubes(start, end) {
    let sum = 0;
    for (let i = start; i <= end; i++) {
        sum += Math.pow(i, 3);
    }
    return sum;
}

function sumOfSquares(start, end) {
    let sum = 0;
    for (let i = start; i <= end; i++) {
        sum += Math.pow(i, 2);
    }
    return sum;
}


let sumA = sumOfCubes(20, 40);
console.log("Сумма кубов всех целых чисел от 20 до 40:", sumA);


let a = parseInt(prompt("Введите значение a (0 < a < 50):"));
if (a > 0 && a < 50) {
    let sumB = sumOfSquares(a, 50);
    console.log(`Сумма квадратов всех целых чисел от ${a} до 50:`, sumB);
} else {
    console.log("Ошибка: a должно быть в диапазоне (0 < a < 50).");
}


let n = parseInt(prompt("Введите значение n (1 <= n <= 100):"));
if (n >= 1 && n <= 100) {
    let sumC = sumOfSquares(1, n);
    console.log(`Сумма квадратов всех целых чисел от 1 до ${n}:`, sumC);
} else {
    console.log("Ошибка: n должно быть в диапазоне (1 <= n <= 100).");
}

let aInput = parseInt(prompt("Введите значение a:"));
let bInput = parseInt(prompt("Введите значение b (b > a):"));
if (bInput > aInput) {
    let sumD = sumOfSquares(aInput, bInput);
    console.log(`Сумма квадратов всех целых чисел от ${aInput} до ${bInput}:`, sumD);
} else {
    console.log("Ошибка: b должно быть больше a.");
}