const prompt = require('prompt-sync')();

function calculateSum() {
    const numbers = [2, 3, 4, 10];
    const numberOfTwos = 10; 
    
    const sumOfNumbers = numbers.reduce((sum, num) => sum + num, 0);
    const sumOfTwos = numberOfTwos * 2;

    return sumOfNumbers + sumOfTwos;
}

const totalSum = calculateSum();
console.log(`Сумма: ${totalSum}`);