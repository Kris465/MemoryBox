const prompt = require('prompt-sync')();

function approximateAreaOfSineArc(n) {
    const a = 0;
    const b = Math.PI;
    const h = (b - a) / n;
    let area = 0.5 * (Math.sin(a) + Math.sin(b));

    for (let i = 1; i < n; i++) {
        const x = a + i * h;
        area += Math.sin(x);
    }

    area *= h;
    return area;
}

const userInput = prompt("Введите количество разбиений (n):");
const n = parseInt(userInput);

if (!isNaN(n) && n > 0) {
    const area = approximateAreaOfSineArc(n);
    console.log(`Приближенная площадь одной арки синусоиды: ${area.toFixed(4)}`);
} else {
    console.log("Пожалуйста, введите корректное натуральное число");
}
    