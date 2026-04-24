const prompt = require('prompt-sync')();

function calculateAverage(numbers) {
    const sum = numbers.reduce((accumulator, current) => accumulator + current, 0);
    const average = sum / numbers.length;
    return average;
}

const n = parseInt(prompt("Введите натуральное число n (количество вещественных чисел):"), 10);

if (isNaN(n) || n <= 0) {
    alert("Пожалуйста, введите корректное натуральное число.");
} else {
    const userInput = prompt(`Введите ${n} вещественных числа через запятую:`);

    const numbers = userInput.split(',').map(Number);

    if (numbers.length !== n || numbers.some(isNaN)) {
        alert(`Пожалуйста, введите ровно ${n} корректных вещественных чисел.`);
    } else {
        const result = calculateAverage(numbers);
        alert(`Среднее арифметическое: ${result}`); 
    }
}