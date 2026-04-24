let sum = 0;

for (let num = 31; num < 100; num++) {

    if (num % 3 === 0) {
   
        const lastDigit = num % 10;
        if (lastDigit === 2 || lastDigit === 4 || lastDigit === 8) {
            sum += num;
        }
    }
}

console.log(`Сумма чисел: ${sum}`);