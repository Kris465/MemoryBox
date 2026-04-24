const prompt = require('prompt-sync')();

function averageOfIntegers(start, end) {
    let sum = 0;
    let count = 0;
    for (let i = start; i <= end; i++) {
        sum += i;
        count++;
    }
    return sum / count;
}

let averageA = averageOfIntegers(1, 1000);
console.log("Среднее арифметическое всех целых чисел от 1 до 1000:", averageA);

let b = parseInt(prompt("Введите значение b (b >= 100):"));
if (b >= 100) {
    let averageB = averageOfIntegers(100, b);
    console.log(`Среднее арифметическое всех целых чисел от 100 до ${b}:`, averageB);
} else {
    console.log("Ошибка: b должно быть больше или равно 100.");
}

let a = parseInt(prompt("Введите значение a (a <= 200):"));
if (a <= 200) {
    let averageC = averageOfIntegers(a, 200);
    console.log(`Среднее арифметическое всех целых чисел от ${a} до 200:`, averageC);
} else {
    console.log("Ошибка: a должно быть меньше или равно 200.");
}

let aInput = parseInt(prompt("Введите значение a:"));
let bInput = parseInt(prompt("Введите значение b (b > a):"));
if (bInput > aInput) {
    let averageD = averageOfIntegers(aInput, bInput);
    console.log(`Среднее арифметическое всех целых чисел от ${aInput} до ${bInput}:`, averageD);
} else {
    console.log("Ошибка: b должно быть больше a.");
}