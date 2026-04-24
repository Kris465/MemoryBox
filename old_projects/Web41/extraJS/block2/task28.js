const prompt = require('prompt-sync')();

let found = false; 

for (let x = 100; x <= 999; x++) {
    const secondDigit = Math.floor((x / 10) % 10); 
    const remainingNumber = x - secondDigit * 10;

    if (10 * remainingNumber + secondDigit === 546) {
        console.log(`Найдено число x: ${x}`);
        found = true; 
        break; 
    }
}
if (!found) {
    console.log("Число x не найдено.");
}