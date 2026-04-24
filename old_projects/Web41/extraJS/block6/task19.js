const prompt = require('prompt-sync')();

let prevNumerator = 1;
let prevDenominator = 1;
let numerator = 2;
let denominator = 1;

while (true) {
    const currentValue = numerator / denominator;
    const previousValue = prevNumerator / prevDenominator;
    if (Math.abs(currentValue - previousValue) <= 0.001) {
        console.log(`Первый член, отличающийся не более чем на 0.001: ${currentValue}`);
        break;
    }
    prevNumerator = numerator;
    prevDenominator = denominator;

    const nextNumerator = numerator + prevNumerator;
    const nextDenominator = denominator + prevDenominator;

    numerator = nextNumerator;
    denominator = nextDenominator;
}