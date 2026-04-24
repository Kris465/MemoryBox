const prompt = require('prompt-sync')();

function canFitCardInEnvelope(a, b, c, d) {

    const availableWidth = a - 2;
    const availableHeight = b - 2;


    return (c <= availableWidth && d <= availableHeight) || (d <= availableWidth && c <= availableHeight);
}


function getInput() {
    const a = parseFloat(prompt("Введите ширину конверта (a) в мм:"));
    const b = parseFloat(prompt("Введите высоту конверта (b) в мм:"));
    const c = parseFloat(prompt("Введите ширину открытки (c) в мм:"));
    const d = parseFloat(prompt("Введите высоту открытки (d) в мм:"));


    if (a <= 0 || b <= 0 || c <= 0 || d <= 0) {
        console.log("Все числа должны быть положительными.");
        return;
    }


    const result = canFitCardInEnvelope(a, b, c, d);
    if (result) {
        console.log(`Открытка размером ${c} x ${d} мм поместится в конверт размером ${a} x ${b} мм.`);
    } else {
        console.log(`Открытка размером ${c} x ${d} мм не поместится в конверт размером ${a} x ${b} мм.`);
    }
}


getInput();