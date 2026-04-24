function calculateSum(start1, end1, start2, end2) {
    let sum = 0;

    for (let i = start1; i <= end1; i++) {
        sum += i;
    }

    for (let j = start2; j <= end2; j++) {
        sum += j;
    }

    return sum;
}

let result = calculateSum(2, 10, 3, 11);
console.log("Сумма последовательности от 2 до 10 и от 3 до 11:", result);