const prompt = require('prompt-sync')();


function calculateTrapezoidArea(a, b, alpha) {
    const alphaRad = (alpha * Math.PI) / 180;

    const h = ((b - a) / 2) * Math.tan(alphaRad);

    const area = ((a + b) / 2) * h;

    return area;
}

const a = prompt("введите первое основание: ");
const b = prompt("введите второе основание: ");
const alpha = prompt("введите больший угол: ");

const result = calculateTrapezoidArea(a, b, alpha);
console.log(`Площадь трапеции: ${result}`);