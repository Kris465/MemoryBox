const prompt = require('prompt-sync')();

function calculateAverages(num1, num2) {

    const absNum1 = Math.abs(num1);
    const absNum2 = Math.abs(num2);

    const arithmeticMean = (absNum1 + absNum2) / 2;
    
    const geometricMean = Math.sqrt(absNum1 * absNum2);
    
    return {
        arithmeticMean: arithmeticMean,
        geometricMean: geometricMean
    };
}

const num1 = prompt('введите число: ')
const num2 = prompt('введите число: ')

const result = calculateAverages(num1, num2);

console.log(`Среднее арифметическое: ${result.arithmeticMean}`);
console.log(`Среднее геометрическое: ${result.geometricMean}`);