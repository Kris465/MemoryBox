const prompt = require('prompt-sync')();

function isLeapYear(year) {
    
    if (year % 4 === 0) {
        if (year % 100 === 0) {
            
            return year % 400 === 0;
        }
        
        return true;
    }
    
    return false;
}


const input = prompt("Введите год:");
const year = parseInt(input);


if (isNaN(year) || year <= 0) {
    console.log("Пожалуйста, введите корректный натуральный год.");
} else {
    
    const result = isLeapYear(year);
    console.log(`Год ${year} ${result ? "является" : "не является"} високосным.`);
}