const prompt = require('prompt-sync')();

const targetNumber = parseInt(prompt("Введите целевое число (например, 654): "));
let found = false; 

for (let x = 100; x <= 999; x++) {
    const lastDigit = x % 10; 
    const remainingNumber = Math.floor(x / 10); 


    const firstDigit = Math.floor(remainingNumber / 10); 
    const secondDigit = remainingNumber % 10; 
    const swappedNumber = secondDigit * 10 + firstDigit; 

  
    if (10 * swappedNumber + lastDigit === targetNumber) {
        console.log(`Найдено число x: ${x}`);
        found = true; 
        break; 
    }
}

if (!found) {
    console.log("Число x не найдено.");
}