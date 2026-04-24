const prompt = require('prompt-sync')();

function calculateSum(a) {
    const constantSum = 2 * 4; 
    const seriesSum = (10 * (10 + 1)) / 2; 
    const additionalTwo = 2; 

    const totalSum = constantSum + seriesSum + additionalTwo + a;
    return totalSum;
}

const a = 5.5; 

const total = calculateSum(a);
console.log(`Сумма: ${total}`);