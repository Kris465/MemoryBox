const prompt = require('prompt-sync')();

function sumOfRealNumbers(n, numbers) {
    if (n !== numbers.length) {
        console.error("Количество элементов в массиве не соответствует значению n.");
        return null;
    }

    const sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0);

    return sum;
}

const n = 5; 
const realNumbers = [1.5, 2.3, 3.7, 4.1, 5.6]; 
const result = sumOfRealNumbers(n, realNumbers);
if (result !== null) {
    console.log("Сумма всех вещественных чисел:", result);
}