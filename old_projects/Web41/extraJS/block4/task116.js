const prompt = require('prompt-sync')();

function calculateDifference(a1, a2, b) {
    const twoDigitNumber = 21 * 10 + a1; 
    const singleDigitNumber = b; 
    const difference = twoDigitNumber - singleDigitNumber;
    const tens = Math.floor(difference / 10); 
    const units = difference % 10; 

    return { tens, units };
}

const a1 = parseInt(prompt("Введите первую цифру (единицы):"), 10); 
const a2 = parseInt(prompt("Введите вторую цифру (десятки):"), 10); 
const b = parseInt(prompt("Введите однозначное число (b):"), 10); 

const result = calculateDifference(a1, a2, b);
console.log(`Разность: Десятки: ${result.tens}, Единицы: ${result.units}`);