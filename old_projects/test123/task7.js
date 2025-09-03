const prompt = require('prompt-sync')();

function mean() {
    const numbers = [];

    function avg(...args) {
        const sum = numbers.reduce((a, b) => a + b);
        const avg = sum / numbers.length;
        return avg;
    }

    while (true) {
        const input = prompt('Введите число (или "стоп" для завершения): ');

        if (input.toLowerCase() === 'stop') {
            break;
        }

        const number = parseFloat(input);

        if (!isNaN(number)) {
            numbers.push(number);
        } else {
            console.log('Пожалуйста, введите корректное число или "стоп".');
        }
    }
    
    if (numbers.length > 0) {
        console.log(`Среднее значение: ${avg(...numbers)}`);
    } else {
        console.log('Не было введено ни одного числа.');
    }
}

mean();