const prompt = require('prompt-sync')();

function calculateDifference(a1, a2, b1, b2) {

    const firstNumber = a2 * 10 + a1; 
    const secondNumber = b2 * 10 + b1; 


    const difference = firstNumber - secondNumber;

    
    const tens = Math.floor(difference / 10); 
    const units = difference % 10; 

    return { tens, units };
}


const a1 = parseInt(prompt("Введите первую цифру (единицы первого числа):"), 10); 
const a2 = parseInt(prompt("Введите вторую цифру (десятки первого числа):"), 10); 
const b1 = parseInt(prompt("Введите первую цифру (единицы второго числа):"), 10); 
const b2 = parseInt(prompt("Введите вторую цифру (десятки второго числа):"), 10); 

const result = calculateDifference(a1, a2, b1, b2);
console.log(`Разность: Десятки: ${result.tens}, Единицы: ${result.units}`);