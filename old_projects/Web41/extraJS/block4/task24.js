const prompt = require('prompt-sync')();

function checkNumberEquality(number) {

    if (number < 10 || number > 99) {
        console.log("Пожалуйста, введите двузначное число.");
        return;
    }


    let firstDigit = Math.floor(number / 10); 
    let secondDigit = number % 10; 

   
    let square = number * number;


    let sumOfCubes = 4 * (Math.pow(firstDigit, 3) + Math.pow(secondDigit, 3));


    if (square === sumOfCubes) {
        console.log(`Для числа ${number}: квадрат (${square}) равен учетверенной сумме кубов цифр (${sumOfCubes}). Ответ: положительный.`);
    } else {
        console.log(`Для числа ${number}: квадрат (${square}) не равен учетверенной сумме кубов цифр (${sumOfCubes}). Ответ: отрицательный.`);
    }
}


let number = parseInt(prompt("Введите двузначное число:"));

if (!isNaN(number)) {
    checkNumberEquality(number);
} else {
    console.log("Пожалуйста, введите корректное число.");
}