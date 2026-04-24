const prompt = require('prompt-sync')();

function calculateSum(a1, a2, a3, b1, b2) {
    
    const threeDigitNumber = a3 * 100 + a2 * 10 + a1;
    
    const twoDigitNumber = b2 * 10 + b1; 

    
    const sum = threeDigitNumber + twoDigitNumber;

    
    const hundreds = Math.floor(sum / 100); 
    const tens = Math.floor((sum % 100) / 10);
    const units = sum % 10; 

    return { hundreds, tens, units };
}


const a1 = parseInt(prompt("Введите первую цифру (единицы трехзначного числа):"), 10); 
const a2 = parseInt(prompt("Введите вторую цифру (десятки трехзначного числа):"), 10); 
const a3 = parseInt(prompt("Введите третью цифру (сотни трехзначного числа):"), 10);
const b1 = parseInt(prompt("Введите первую цифру (единицы двузначного числа):"), 10); 
const b2 = parseInt(prompt("Введите вторую цифру (десятки двузначного числа):"), 10);

const result = calculateSum(a1, a2, a3, b1, b2);
console.log(`Сумма: Сотни: ${result.hundreds}, Десятки: ${result.tens}, Единицы: ${result.units}`);