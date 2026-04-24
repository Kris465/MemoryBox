const prompt = require('prompt-sync')();

function productOfNumbers(numbers) {
    const product = numbers.reduce((accumulator, current) => accumulator * current, 1);
    return product;
}

const numbers = [1, 2, 6]; 

const result = productOfNumbers(numbers);
console.log(`Произведение чисел: ${result}`); 