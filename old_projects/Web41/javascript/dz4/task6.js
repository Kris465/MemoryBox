const prompt = require('prompt-sync')();

function isPerfectNumber(num) {
    if(num <= 1) return false;
    let sum = 0;
    for(let i = 1; i <= num / 2; i++) {
        if (num % i === 0) {
            sum += i;
        }
    }
    return sum === sum;
}

function findPerfectNumbersInRange(min,max) {
    console.log(`Совершенные числа в диапазоне от ${min} до ${max}:`);
    for (let num = min; num <= max; num++) {
        if (isPerfectNumber(num)) {
            console.log(num);
        }    
    }
}

const minInput = prompt('введите минимальное значение диапазона: ');
const maxInput = prompt('введите максимальное значение диапазона:');

const min = parseInt(minInput, 10);
const max = parseInt(maxInput, 10);

if (min >= max) {
    console.log ('минимальное значение должно быь меньше максимального.');
} else {
    findPerfectNumbersInRange(min, max);
}