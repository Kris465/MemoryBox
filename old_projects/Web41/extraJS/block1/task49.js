const prompt = require('prompt-sync')();


function calculateTrapezoidPerimeter(a, b, h) {
    const side = Math.sqrt(h ** 2 + ((a - b) / 2) ** 2);
    const perimeter = a + b + 2 * side;
    
    return perimeter;
}

const a = prompt("введите первое основание: ");
const b = prompt("введите второе основание: ");
const h = prompt("введите высоту: ");

const perimeter = calculateTrapezoidPerimeter(a, b, h);
console.log(`Периметр трапеции: ${perimeter}`);