const prompt = require('prompt-sync')();

function f(x) {
    return 0.5 * Math.pow(x, 2) + 2;
}

function approximateArea(n) {
    const a = 0;
    const b = 2; 
    const h = (b - a) / n;
    let area = 0;

    for (let i = 0; i < n; i++) {
        const x1 = a + i * h;
        const x2 = a + (i + 1) * h;
        const y1 = f(x1);
        const y2 = f(x2);

        const height1 = Math.max(0, Math.min(y1, 2));
        const height2 = Math.max(0, Math.min(y2, 2));

        area += ((height1 + height2) / 2) * h;
    }

    return area;
}

const userInput = prompt("Введите количество разбиений (n):");
const n = parseInt(userInput);

if (!isNaN(n) && n > 0) {
    const area = approximateArea(n);
    console.log(`Приближенная площадь фигуры: ${area.toFixed(4)}`);
} else {
    console.log("Пожалуйста, введите корректное натуральное число.");
}