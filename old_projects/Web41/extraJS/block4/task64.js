const prompt = require('prompt-sync')();

function isLuckyNumber(n) {

    const numberStr = n.toString();

   
    if (numberStr.length !== 6) {
        return false;
    }

    
    const firstHalfSum = parseInt(numberStr[0]) + parseInt(numberStr[1]) + parseInt(numberStr[2]);
    const secondHalfSum = parseInt(numberStr[3]) + parseInt(numberStr[4]) + parseInt(numberStr[5]);


    return firstHalfSum === secondHalfSum;
}


const input = prompt("Введите шестизначное число:");
const n = parseInt(input);

if (isNaN(n) || n < 100000 || n > 999999) {
    console.log("Пожалуйста, введите корректное шестизначное число.");
} else {
   
    const result = isLuckyNumber(n);
    console.log(`Число ${n} ${result ? "является" : "не является"} счастливым.`);
}