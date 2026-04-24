const prompt = require('prompt-sync')();

function mean(...args) {
    let total = 0;
    let count = 0;

    for (let arg of args) {
        if (typeof arg === 'number') { 
            total += arg;
            count++;
        }
    }

    return count > 0 ? total / count : 0; 
}

function main() {
    const inputs = [];

    console.log("введите числа (для завершения ввода введите 'exit'):");
    while (true) {
        const input = prompt('>');
        if (input.toLowerCase() === 'exit') {
            break;
        }
        const number = parseFloat(input);
        if (!isNaN(number)) {
            inputs.push(number);
        } else {
            console.log("пожалуйста введите число или 'exit' для завершения.");
        }
    }
    const count = mean(...inputs);
        console.log(`среднее значение введенных чисел: ${count}`);
}

main();