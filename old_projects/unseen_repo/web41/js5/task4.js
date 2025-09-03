const prompt = require('prompt-sync')();

function mean(...args) {
    let sum = 0;
    let count = 0;

    for (const arg of args) {
        if (typeof arg === 'number') {
            sum += arg;
            count++;
        }
    }

    return count === 0 ? 0 : sum / count;
}

function main() {
    const inputs = [];

    console.log("Введите значения (для завершения ввода введите 'exit'):");

    while (true) {
        const input = prompt('> ');

        if (input.toLowerCase() === 'exit') {
            break;
        }

        const number = parseFloat(input);

        if (!isNaN(number)) {
            inputs.push(number);
        } else {
            inputs.push(input);
        }
    }

    const average = mean(...inputs);
    console.log(`Среднее значение введенных чисел: ${average}`);
}

main();
