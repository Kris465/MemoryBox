const prompt = require('prompt-sync')();

function checkIntervals(numbers) {
    const interval1 = [1.6, 3.8];
    const interval2 = [0.7, 5.1];

    const inInterval1 = numbers.filter(num => num > interval1[0] && num < interval1[1]);
    const inInterval2 = numbers.filter(num => num > interval2[0] && num < interval2[1]);

    console.log("Числа в интервале (1.6, 3.8):", inInterval1);
    console.log("Числа в интервале (0.7, 5.1):", inInterval2);
}
const numbers = [parseFloat(prompt("Введите первое число:")),
                 parseFloat(prompt("Введите второе число:")),
                 parseFloat(prompt("Введите третье число:"))];

checkIntervals(numbers);