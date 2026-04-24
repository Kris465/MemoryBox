const prompt = require('prompt-sync')();

function isTriangle(a, b, c) {

    return (a + b > c) && (a + c > b) && (b + c > a);
}

function isRightTriangle(a, b, c) {
    
    const sides = [a, b, c].sort((x, y) => x - y);
    const [x, y, z] = sides;

    return Math.abs(x * x + y * y - z * z) < 1e-10; 
}


const a = parseFloat(prompt("Введите длину стороны a (положительное вещественное число):"));
const b = parseFloat(prompt("Введите длину стороны b (положительное вещественное число):"));
const c = parseFloat(prompt("Введите длину стороны c (положительное вещественное число):"));


if (isTriangle(a, b, c)) {
    if (isRightTriangle(a, b, c)) {
        console.log(`Треугольник со сторонами ${a}, ${b}, ${c} является прямоугольным.`);
    } else {
        console.log(`Треугольник со сторонами ${a}, ${b}, ${c} не является прямоугольным.`);
    }
} else {
    console.log(`Треугольник со сторонами ${a}, ${b}, ${c} не существует.`);
}