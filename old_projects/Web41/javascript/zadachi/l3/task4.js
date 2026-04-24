const prompt = require('prompt-sync')();
let procent = prompt('введите процент ставки: ');
let years = 0;
let summa = 1;
while (summa < 2) {
    summa *= (1 + procent / 100 );
    years ++;
} 
console.log(`количество лет: ${years}`);