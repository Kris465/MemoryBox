function calculateSum() {
    let sum = 0;

    sum += 2;
    sum += 8;

    for (let i = 0; i < 4; i++) {
        sum += 1;
    }

    for (let j = 0; j < 3; j++) {
        sum += 3;
    }

    return sum;
}

let result = calculateSum();
console.log("Сумма:", result);