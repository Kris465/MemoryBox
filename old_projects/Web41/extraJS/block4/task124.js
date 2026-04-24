const prompt = require('prompt-sync')();

function isTriangle(a, b, c) {
    return (a + b > c) && (a + c > b) && (b + c > a);
}

function triangleType(a, b, c) {
    const sides = [a, b, c].sort((x, y) => x - y);
    const [x, y, z] = sides;

    if (Math.abs(x * x + y * y - z * z) < 1e-10) {
        return "прямоугольный";
    } else if (x * x + y * y > z * z) {
        return "остроугольный";
    } else {
        return "тупоугольный";
    }
}

function triangleProperties(a, b, c) {
    if (a === b && b === c) {
        return "равносторонний";
    } else if (a === b || b === c || a === c) {
        return "равнобедренный";
    } else {
        return "разносторонний";
    }
}

const a = parseFloat(prompt("Введите длину стороны a (положительное вещественное число):"));
const b = parseFloat(prompt("Введите длину стороны b (положительное вещественное число):"));
const c = parseFloat(prompt("Введите длину стороны c (положительное вещественное число):"));

if (isTriangle(a, b, c)) {
    const type = triangleType(a, b, c);
    const properties = triangleProperties(a, b, c);
    
    console.log(`Треугольник со сторонами ${a}, ${b}, ${c} является ${type} и ${properties}.`);
} else {
    console.log(`Треугольник со сторонами ${a}, ${b}, ${c} не существует.`);
}