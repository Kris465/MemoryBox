const prompt = require('prompt-sync')();

function numbers(...args) {
    let count = 0;

    for (const arg of args) {
        if (typeof arg === 'number') {
            count++;
        }
    }

    return count;
}

function main() {
    const inputs = [];

    console.log("Введите числа (для завершения ввода введите 'exit'):");

    while (true) {
        const input = prompt('> ');

        if (input.toLowerCase() === 'exit') {
            break;
        }

        const number = parseFloat(input);

        if (!isNaN(number)) {
            inputs.push(number);
        } else {
            console.log("Пожалуйста, введите число или 'exit' для завершения.");
        }
    }

    const count = numbers(...inputs);
    console.log(`Количество введенных чисел: ${count}`);
}

main();
