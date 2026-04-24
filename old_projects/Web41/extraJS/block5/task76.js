const prompt = require('prompt-sync')();

function calculatePowers(a, n) {
    const results = [];
    let currentPower = a;

    for (let i = 1; i <= n; i++) {
        results.push(currentPower); 
        currentPower *= a; 
    }

    return results;
}

const a = 2.5; 
const n = 5;   

const powers = calculatePowers(a, n);
console.log(`Значения a в степенях от 1 до ${n}:`, powers);