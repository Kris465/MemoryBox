const prompt = require('prompt-sync')();

function findMinimum(...args) {
    return Math.min(...args);
}

function collectNumbers() {
    const numbers = [];

    while (true) {
        const input = prompt('Введите число (или stop для завершения): ');

        if (input.toLowerCase() === "stop") {
            break; 
        }

        const number = parseFloat(input);

        if (!isNaN(number)) {
            numbers.push(number);
        } else {
            console.log("Введите коректное число или stop: ");

        }
    }

    if (numbers.length > 0) {
        console.log(`Минимальное значение: ${findMinimum(...numbers)}`);
    } else {
        console.log('Не было введено ни одного числа.');
    }
}


collectNumbers();



















