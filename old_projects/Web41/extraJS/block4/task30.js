const prompt = require('prompt-sync')();


function analyzeNumber(number) {
    
   


    if (number < 100 || number > 999) {
        console.log("Пожалуйста, введите трехзначное число.");
        return;
    }

    let firstDigit = Math.floor(number / 100);
    let secondDigit = Math.floor((number % 100) / 10); 
    let lastDigit = number % 10; 

   
    let sumOfDigits = firstDigit + secondDigit + lastDigit;
    let productOfDigits = firstDigit * secondDigit * lastDigit;

    if (sumOfDigits >= 10 && sumOfDigits < 100) {
        console.log(`Сумма цифр (${sumOfDigits}) является двузначным числом.`);
    } else {
        console.log(`Сумма цифр (${sumOfDigits}) не является двузначным числом.`);
    }


    if (productOfDigits >= 100 && productOfDigits < 1000) {
        console.log(`Произведение цифр (${productOfDigits}) является трехзначным числом.`);
    } else {
        console.log(`Произведение цифр (${productOfDigits}) не является трехзначным числом.`);
    }

    if (sumOfDigits > productOfDigits) {
        console.log(`Сумма цифр (${sumOfDigits}) больше произведения цифр (${productOfDigits}).`);
    } else if (sumOfDigits < productOfDigits) {
        console.log(`Сумма цифр (${sumOfDigits}) меньше произведения цифр (${productOfDigits}).`);
    } else {
        console.log(`Сумма цифр (${sumOfDigits}) равна произведению цифр (${productOfDigits}).`);
    }


    if (sumOfDigits % 5 === 0) {
        console.log(`Сумма цифр (${sumOfDigits}) кратна пяти.`);
    } else {
        console.log(`Сумма цифр (${sumOfDigits}) не кратна пяти.`);
    }

    
    if (firstDigit !== 0 && sumOfDigits % firstDigit === 0) {
        console.log(`Сумма цифр (${sumOfDigits}) кратна первой цифре (${firstDigit}).`);
    } else {
        console.log(`Сумма цифр (${sumOfDigits}) не кратна первой цифре (${firstDigit}).`);
    }
}

let number = parseInt(prompt("Введите трехзначное число:"));


if (!isNaN(number)) {
    analyzeNumber(number);
} else {
    console.log("Пожалуйста, введите корректное число.");
}