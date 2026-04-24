const prompt = require('prompt-sync')();

function findRoots(a, b, c) {

    const D = b * b - 4 * a * c;

    if (D > 0) {

        const root1 = (-b + Math.sqrt(D)) / (2 * a);
        const root2 = (-b - Math.sqrt(D)) / (2 * a);
        return `Уравнение имеет два различных вещественных корня: x1 = ${root1}, x2 = ${root2}`;
    } else if (D === 0) {

        const root = -b / (2 * a);
        return `Уравнение имеет один двойной вещественный корень: x = ${root}`;
    } else {

        return "Уравнение не имеет вещественных корней.";
    }
}


const a = parseFloat(prompt("Введите значение a (a > 0):"));
const b = parseFloat(prompt("Введите значение b:"));
const c = parseFloat(prompt("Введите значение c (c > 0):"));


if (a <= 0 || c <= 0) {
    console.log("Значения должны быть: a > 0 и c > 0.");
} else {

    const result = findRoots(a, b, c);
    console.log(result);
}