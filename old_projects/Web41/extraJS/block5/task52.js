const prompt = require('prompt-sync')();

function calculateAverage(grades) {
    const sum = grades.reduce((accumulator, current) => accumulator + current, 0);
    const average = sum / grades.length;
    return average;
}

const userInput = prompt("Введите оценки по физике для 20 учеников через запятую (например: 5,4,3,2,...):");

const grades = userInput.split(',').map(Number);

if (grades.length !== 20 || grades.some(isNaN)) {
    alert("Пожалуйста, введите ровно 20 корректных оценок.");
} else {
    const result = calculateAverage(grades);
    alert(`Средняя оценка по физике: ${result}`);
}