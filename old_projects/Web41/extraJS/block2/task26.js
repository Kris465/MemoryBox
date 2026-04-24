const prompt = require('prompt-sync')();

let found = false; 

for (let x = 100; x <= 999; x++) {
    const firstDigit = Math.floor(x / 100); 
    const remainingNumber = x % 100; 

    if (10 * remainingNumber + firstDigit === 564) {
        console.log(`Найдено число x: ${x}`);
        found = true;
        break; 
    }
}

if (!found) {
    console.log("Число x не найдено.");
}