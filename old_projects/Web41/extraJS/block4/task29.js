const prompt = require('prompt-sync')();

function checkSquareAndCubes(number) {
   
    if (number < 100 || number > 999) {
        console.log("Пожалуйста, введите трехзначное число.");
        return;
    }

   
    let firstDigit = Math.floor(number / 100); 
    let secondDigit = Math.floor((number % 100) / 10); 
    let lastDigit = number % 10; 

    
    let square = number * number;


    let sumOfCubes = Math.pow(firstDigit, 3) + Math.pow(secondDigit, 3) + Math.pow(lastDigit, 3);

    
    if (square === sumOfCubes) {
        console.log(`Квадрат числа ${number} (${square}) равен сумме кубов его цифр (${sumOfCubes}).`);
    } else {
        console.log(`Квадрат числа ${number} (${square}) не равен сумме кубов его цифр (${sumOfCubes}).`);
    }
}


let number = parseInt(prompt("Введите трехзначное число:"));


if (!isNaN(number)) {
    checkSquareAndCubes(number);
} else {
    console.log("Пожалуйста, введите корректное число.");
}