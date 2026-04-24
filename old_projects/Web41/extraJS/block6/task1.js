const prompt = require('prompt-sync')();

function processSequence() {
    let sum = 0;
    let count = 0;
    let number;

    do {
        number = parseInt(prompt("Введите число (0 для завершения):"));

        if (!isNaN(number)) {
            sum += number;
            if (number !== 0) {
                count++;
            }
        } else {
            alert("Пожалуйста, введите целое число.");
        }
    } while (number !== 0);

    return { sum, count };
}

const result = processSequence();
console.log(`Сумма всех чисел: ${result.sum}`);
console.log(`Количество всех чисел: ${result.count}`);