const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите натуральное число:"), 10);
const d = parseInt(prompt("Введите число d для сравнения с делителями:"), 10);

const divisors = [];
let sumDivisors = 0;
let sumEvenDivisors = 0;
let countDivisors = 0;
let countOddDivisors = 0;
let countEvenDivisors2 = 0;
let countGreaterD = 0;

for (let i = 1; i <= n; i++) {
    if (n % i === 0) {
        divisors.push(i);
        sumDivisors += i;
        countDivisors++;
        if (i % 2 === 0) {
            sumEvenDivisors += i;
            countEvenDivisors2++;
        } else {
            countOddDivisors++;
        }
        if (i > d) {
            countGreaterD++;
        }
    }
}

console.log("Делители:", divisors);
console.log("Сумма делителей:", sumDivisors);
console.log("Сумма четных делителей:", sumEvenDivisors);
console.log("Количество делителей:", countDivisors);
console.log("Количество нечетных делителей:", countOddDivisors);
console.log("Количество делителей, больших " + d + ":", countGreaterD);