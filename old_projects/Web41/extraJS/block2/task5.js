const prompt = require('prompt-sync')();

function calculateFullWeeks(days) {
    const fullWeeks = Math.floor(days / 7);
    return fullWeeks;
}

const daysPassed = 234;

const result = calculateFullWeeks(daysPassed);
console.log(`Количество полных недель: ${result}`);