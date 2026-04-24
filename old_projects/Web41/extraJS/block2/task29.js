const readline = require('readline');


const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function findOriginalNumber(n) {
    
    if (n < 10 || n > 999 || Math.floor(n / 10) % 10 === 0) {
        console.log("Число n должно быть в диапазоне от 10 до 999 и не иметь нулей в десятках.");
        return;
    }

    const hundreds = Math.floor(n / 100); 
    const tens = Math.floor((n % 100) / 10);
    const units = n % 10; 
   
    const originalNumber = 100 * tens + 10 * hundreds + units;

    console.log(`Исходное трехзначное число x: ${originalNumber}`);
}


rl.question("Введите число n (10 ≤ n ≤ 999, десятки не равны нулю): ", (input) => {
    const n = parseInt(input, 10);
    findOriginalNumber(n);
    rl.close(); 
});