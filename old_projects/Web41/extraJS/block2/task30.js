const prompt = require('prompt-sync')();

const targetNumber = parseInt(prompt("Введите целевое число (например, 456): "));
let found = false;

for (let x = 100; x <= 999; x++) {
    const secondDigit = Math.floor((x / 10) % 10); 
    const remainingNumber = Math.floor(x / 100) * 10 + (x % 10); 


    if (10 * remainingNumber + secondDigit === targetNumber) {
        console.log(`Найдено число x: ${x}`);
        found = true; 
        break; 
    }
}

if (!found) {
    console.log("Число x не найдено.");
}