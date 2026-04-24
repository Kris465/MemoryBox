const prompt = require('prompt-sync')();

const num1 = prompt("Введите число: ");

const number = num1;

const factors = kishechniPalochki(number);

function kishechniPalochki(n, divisor = 2) {

    if (n === 1) {
        return [];
    }

    if (n % divisor === 0) {
        return[divisor].concat(kishechniPalochki(n / divisor, divisor));
    } 
    else {

        return kishechniPalochki(n, divisor + 1);
    }
}

console.log(factors);



