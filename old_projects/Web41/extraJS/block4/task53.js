const prompt = require('prompt-sync')();

function canBrickFitThroughHole(a, b, c, x, y) {
    return (
        (a <= x && b <= y) || (a <= y && b <= x) ||
        (a <= x && c <= y) || (a <= y && c <= x) ||
        (b <= x && c <= y) || (b <= y && c <= x)
    );
}

function getInput() {
    const a = parseFloat(prompt("Введите размер a кирпича:"));
    const b = parseFloat(prompt("Введите размер b кирпича:"));
    const c = parseFloat(prompt("Введите размер c кирпича:"));
    const x = parseFloat(prompt("Введите ширину отверстия x:"));
    const y = parseFloat(prompt("Введите высоту отверстия y:"));

    if (a <= 0 || b <= 0 || c <= 0 || x <= 0 || y <= 0) {
        console.log("Все числа должны быть положительными.");
        return;
    }

    const result = canBrickFitThroughHole(a, b, c, x, y);
    if (result) {
        console.log(`Кирпич с размерами ${a} x ${b} x ${c} пройдет через отверстие ${x} x ${y}.`);
    } else {
        console.log(`Кирпич с размерами ${a} x ${b} x ${c} не пройдет через отверстие ${x} x ${y}.`);
    }
}

getInput();