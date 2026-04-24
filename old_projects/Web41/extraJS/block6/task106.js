
let a = 17;
let b = 4;

function integerDivision(dividend, divisor) {
    const sign = (dividend < 0) ^ (divisor < 0) ? -1 : 1;
    let absDividend = Math.abs(dividend);
    let absDivisor = Math.abs(divisor);
    let quotient = 0;

    while (absDividend >= absDivisor) {
        absDividend -= absDivisor;
        quotient++;
    }

    return sign * quotient;
}

function remainder(dividend, divisor) {
    const sign = dividend < 0 ? -1 : 1;
    let absDividend = Math.abs(dividend);
    let absDivisor = Math.abs(divisor);

    while (absDividend >= absDivisor) {
        absDividend -= absDivisor;
    }

    return sign * absDividend;
}

const resultDivision = integerDivision(a, b);

const resultRemainder = remainder(a, b);

console.log(`Результат целочисленного деления ${a} на ${b} равен: ${resultDivision}`);
console.log(`Остаток от деления ${a} на ${b} равен: ${resultRemainder}`);