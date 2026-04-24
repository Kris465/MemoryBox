const prompt = require('prompt-sync')();

function calculateAverage(numbers) {

    const sum = numbers.reduce((accumulator, current) => accumulator + current, 0);
    const average = sum / numbers.length;
    return average;
}


const userInput = prompt("Введите числа через запятую (например: 1,2,10):");


const numbers = userInput.split(',').map(Number);


if (numbers.length === 0 || numbers.some(isNaN)) {
    alert("Пожалуйста, введите корректные числа.");
} else {
    const result = calculateAverage(numbers);
    alert(`Среднее арифметическое: ${result}`); 
}