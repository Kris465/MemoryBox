
let count = 0;

for (let num = 100; num <= 500; num++) {
 
    const hundreds = Math.floor(num / 100);
    const tens = Math.floor((num % 100) / 10);
    const units = num % 10;

    if (hundreds + tens + units === 15) {
        count++;
    }
}

console.log("Количество чисел:", count);