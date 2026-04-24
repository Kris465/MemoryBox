const prompt = require('prompt-sync')();

function findMaxMin(a, b, c, d) {

    const maxAB = (a > b) ? a : b; 
    const maxCD = (c > d) ? c : d; 
    const max = (maxAB > maxCD) ? maxAB : maxCD; 

   
    const minAB = (a < b) ? a : b;
    const minCD = (c < d) ? c : d; 
    const min = (minAB < minCD) ? minAB : minCD; 

  
    return { max, min };
}


const num1 = parseFloat(prompt("Введите первое вещественное число:"));
const num2 = parseFloat(prompt("Введите второе вещественное число:"));
const num3 = parseFloat(prompt("Введите третье вещественное число:"));
const num4 = parseFloat(prompt("Введите четвертое вещественное число:"));


if (num1 !== num2 && num1 !== num3 && num1 !== num4 &&
    num2 !== num3 && num2 !== num4 &&
    num3 !== num4) {
    
    const result = findMaxMin(num1, num2, num3, num4);
    console.log(`Наибольшее: ${result.max}, Наименьшее: ${result.min}`);
} else {
    console.log("Числа должны быть различными. Пожалуйста, попробуйте снова.");
}