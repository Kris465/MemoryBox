const prompt = require('prompt-sync')();


function calculateSumAndProduct(num) {
    let sum = 0;
    let product = 1;
    

    let numString = num.toString();
    
    for (let i = 0; i < numString.length; i++) {
        let digit = parseInt(numString[i]);
        sum += digit;
        product *= digit;
    }
    
    return { sum, product };
}


let userInput = prompt("Введите четырехзначное число:");

if (userInput !== null) {
    let number = parseInt(userInput);
    

    if (number >= 1000 && number <= 9999) {
        let result = calculateSumAndProduct(number);
        console.log(`Сумма цифр: ${result.sum}`);
        console.log(`Произведение цифр: ${result.product}`);
    } else {
        console.log("Пожалуйста, введите корректное четырехзначное число.");
    }
} else {
    console.log("Ввод отменен.");
}
