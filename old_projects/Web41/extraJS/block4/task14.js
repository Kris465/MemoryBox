const prompt = require('prompt-sync')();

function findRealRoots(a, b, c) {
    const D = b * b - 4 * a * c;

    if (D > 0) {
        const x1 = (-b + Math.sqrt(D)) / (2 * a);
        const x2 = (-b - Math.sqrt(D)) / (2 * a);
        console.log(`Уравнение имеет два различных вещественных корня: x1 = ${x1}, x2 = ${x2}`);
    } else {
        console.log("Уравнение не имеет вещественных корней.");
    }
}

const a = parseFloat(prompt("Введите значение a (a > 0):"));
if (a <= 0) {
    console.log("Значение a должно быть больше 0.");
} else {
    const b = parseFloat(prompt("Введите значение b:"));
    const c = parseFloat(prompt("Введите значение c:"));

    findRealRoots(a, b, c);
}