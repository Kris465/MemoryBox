const prompt = require('prompt-sync')();

function generateFractions(n) {
    const numerators = [1, 2];
    const denominators = [1, 1];
    
    for (let i = 2; i < n; i++) {
        numerators[i] = numerators[i - 1] + numerators[i - 2];
        denominators[i] = denominators[i - 1] + denominators[i - 2];
    }
    
    return { numerators, denominators };
}

function getKthFraction(k) {
    const { numerators, denominators } = generateFractions(k);
    return `${numerators[k - 1]}/${denominators[k - 1]}`;
}

function isSumGreaterThanA(n, A) {
    const { numerators, denominators } = generateFractions(n);
    let sum = 0;
    
    for (let i = 0; i < n; i++) {
        sum += numerators[i] / denominators[i];
    }
    
    return sum > A;
}

const n = 10;
const k = 5;
const A = 10;

const kthFraction = getKthFraction(k);
const firstNFractions = generateFractions(n);
const sumIsGreaterThanA = isSumGreaterThanA(n, A);

console.log(`k-й член последовательности: ${kthFraction}`);
console.log(`Первые n членов последовательности:`);
for (let i = 0; i < n; i++) {
    console.log(`${firstNFractions.numerators[i]}/${firstNFractions.denominators[i]}`);
}
console.log(`Сумма первых n членов больше числа A: ${sumIsGreaterThanA}`);