const prompt = require('prompt-sync')();

const num1 = prompt("Введите число: ");

function Chinazes(number, divisor = 2) {
    if(number <= 1){
        return false;
    }

    if(number <= 3){
        return true;
    }
  
    if(number % 2 === 0 || number % 3 === 0){
        return false;
    }

    if(divisor * divisor > number){
        return true;
    }

    if (number % divisor === 0) {
        return false;
    }
return Chinazes(number, divisor + 6 > 5? divisor + 6: (divisor + 2));
}


console.log(`${Chinazes(num1)}`)