function sumOfSquares(n) {
    let totalSum = 0;

    for (let i = 1; i <= n; i++) {
        let square = 0;
        let oddNumber = 1;

        for (let j = 0; j < i; j++) {
            square += oddNumber;
            oddNumber += 2;
        }

        totalSum += square;
    }

    return totalSum;
}

const n = 10;
const result = sumOfSquares(n);
console.log(`Сумма квадратов первых ${n} натуральных чисел равна ${result}`);