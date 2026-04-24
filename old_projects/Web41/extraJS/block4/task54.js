const prompt = require('prompt-sync')();

function canBoxFitInSuitcase(a, b) {

    return (
        (b[0] <= a[0] && b[1] <= a[1] && b[2] <= a[2]) ||
        (b[0] <= a[0] && b[1] <= a[2] && b[2] <= a[1]) ||
        (b[0] <= a[1] && b[1] <= a[0] && b[2] <= a[2]) ||
        (b[0] <= a[1] && b[1] <= a[2] && b[2] <= a[0]) ||
        (b[0] <= a[2] && b[1] <= a[0] && b[2] <= a[1]) ||
        (b[0] <= a[2] && b[1] <= a[1] && b[2] <= a[0])
    );
}

function getInput() {
    const a1 = parseFloat(prompt("Введите размер a1 чемодана:"));
    const a2 = parseFloat(prompt("Введите размер a2 чемодана:"));
    const a3 = parseFloat(prompt("Введите размер a3 чемодана:"));
    const b1 = parseFloat(prompt("Введите размер b1 коробки:"));
    const b2 = parseFloat(prompt("Введите размер b2 коробки:"));
    const b3 = parseFloat(prompt("Введите размер b3 коробки:"));

    // Проверяем, что все числа положительные
    if (a1 <= 0 || a2 <= 0 || a3 <= 0 || b1 <= 0 || b2 <= 0 || b3 <= 0) {
        console.log("Все числа должны быть положительными.");
        return;
    }

    const result = canBoxFitInSuitcase([a1, a2, a3], [b1, b2, b3]);
    if (result) {
        console.log(`Коробка с размерами ${b1} x ${b2} x ${b3} поместится в чемодан ${a1} x ${a2} x ${a3}.`);
    } else {
        console.log(`Коробка с размерами ${b1} x ${b2} x ${b3} не поместится в чемодан ${a1} x ${a2} x ${a3}.`);
    }
}

getInput();