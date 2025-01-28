const prompt = require('prompt-sync')(); 

const n = prompt('Передайте число: ');

function getFactors(n) {
    if (n <= 0) {
        return "Введите положительное число.";
    }

    const factors = [];
    for (let i = 2; i <= n; i++) {
        while (n % i === 0) {
            factors.push(i);
            n /= i; 
        }
    }
    
    return factors;
}

console.log(`Множители числа ${n}: ${getFactors(n)}`);