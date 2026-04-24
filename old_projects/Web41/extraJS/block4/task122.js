const prompt = require('prompt-sync')();

function isTriangle(a, b, c) {
    
    return (a + b > c) && (a + c > b) && (b + c > a);
}

const a = parseFloat(prompt("Введите длину стороны a (положительное вещественное число):"));
const b = parseFloat(prompt("Введите длину стороны b (положительное вещественное число):"));
const c = parseFloat(prompt("Введите длину стороны c (положительное вещественное число):"));


if (isTriangle(a, b, c)) {
    console.log(`Треугольник со сторонами ${a}, ${b}, ${c} существует.`);
} else {
    console.log(`Треугольник со сторонами ${a}, ${b}, ${c} не существует.`);
}