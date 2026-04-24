const prompt = require("prompt-sync")();


function checkConditions(x, y) {
    return x > 3 && y > 2;
}

let x = parseFloat(prompt("Введите значение x:"));
let y = parseFloat(prompt("Введите значение y:"));

if (!isNaN(x) && isFinite(x) && !isNaN(y) && isFinite(y)) {
    if (checkConditions(x, y)) {
        console.log(`Условия выполнены: x > 3 и y > 2.`);
    } else {
        console.log(`Условия не выполнены: x <= 3 или y <= 2.`);
    }
} else {
    throw new Error("Пожалуйста, введите корректные числа.");
}