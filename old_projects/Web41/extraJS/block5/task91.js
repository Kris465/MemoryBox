const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите натуральное число n (1 < n < 10):"));

if (n > 1 && n < 10) {
    let sumOfSquares = 0;
    let sumOfCubes = 0;
    let sumOfSine = 0;
    let sumOfCosine = 0;

    for (let k = 1; k <= n; k++) {
        sumOfSquares += k * k;
        sumOfCubes += k * k * k;
        sumOfSine += Math.sin(k);
        sumOfCosine += Math.cos(k);
    }

    console.log(`Сумма квадратов от 1 до ${n}: ${sumOfSquares}`);
    console.log(`Сумма кубов от 1 до ${n}: ${sumOfCubes}`);
    console.log(`Сумма синусов от 1 до ${n}: ${sumOfSine}`);
    console.log(`Сумма косинусов от 1 до ${n}: ${sumOfCosine}`);
} else {
    console.log("Пожалуйста, введите корректное значение для n.");
}