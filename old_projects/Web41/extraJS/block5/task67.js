function fibonacci(n) {
    const fib = [1, 1];
    for (let i = 2; i < n; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
    return fib;
}

function getKthFibonacci(k) {
    const fib = fibonacci(k);
    return fib[k - 1];
}

function isSumEven(n) {
    const fib = fibonacci(n);
    const sum = fib.reduce((acc, val) => acc + val, 0);
    return sum % 2 === 0;
}

const n = 10;
const k = 5;

const kthFibonacci = getKthFibonacci(k);
const firstNFibonacci = fibonacci(n);
const sumIsEven = isSumEven(n);

console.log(`k-й член последовательности Фибоначчи (k=${k}): ${kthFibonacci}`);
console.log(`Первые n членов последовательности Фибоначчи (n=${n}): ${firstNFibonacci}`);
console.log(`Сумма первых n членов последовательности Фибоначчи четное число: ${sumIsEven}`);