const prompt = require('prompt-sync')();

function canVasyaFitHeadInWindow(a, b, d) {
    const availableWidth = a - 2;
    const availableHeight = b - 2;

    return d <= availableWidth && d <= availableHeight;
}

function getInput() {
    const a = parseFloat(prompt("Введите ширину форточки (a) в см:"));
    const b = parseFloat(prompt("Введите высоту форточки (b) в см:"));
    const d = parseFloat(prompt("Введите диаметр головы Васи (d) в см:"));

    if (a <= 0 || b <= 0 || d <= 0) {
        console.log("Все числа должны быть положительными.");
        return;
    }

    const result = canVasyaFitHeadInWindow(a, b, d);
    if (result) {
        console.log(`Вася сможет высунуть голову диаметром ${d} см в форточку размером ${a} x ${b} см.`);
    } else {
        console.log(`Вася не сможет высунуть голову диаметром ${d} см в форточку размером ${a} x ${b} см.`);
    }
}


getInput();