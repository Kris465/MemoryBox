const prompt = require('prompt-sync')();

console.log("а) Все целые числа от 20 до 35:");
for (let i = 20; i <= 35; i++) {
    console.log(i);
}

let b = parseInt(prompt("Введите значение b (b > 10):"), 10);
if (b > 10) {
    console.log("\nб) Квадраты всех целых чисел от 10 до " + b + ":");
    for (let i = 10; i <= b; i++) {
        console.log(i * i);
    }
} else {
    console.log("Ошибка: b должно быть больше 10.");
}

let a = parseInt(prompt("Введите значение a (a < 50):"), 10);
if (a < 50) {
    console.log("\nв) Третьи степени всех целых чисел от " + a + " до 50:");
    for (let i = a; i <= 50; i++) {
        console.log(i * i * i); 
    }
} else {
    console.log("Ошибка: a должно быть меньше 50.");
}

a = parseInt(prompt("Введите значение a:"), 10);
b = parseInt(prompt("Введите значение b (b > a):"), 10);
if (b > a) {
    console.log("\nг) Все целые числа от " + a + " до " + b + ":");
    for (let i = a; i <= b; i++) {
        console.log(i);
    }
} else {
    console.log("Ошибка: b должно быть больше a.");
}