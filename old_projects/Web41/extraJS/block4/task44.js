const prompt = require('prompt-sync')();

function checkRemainder(a, b, c, d) {
    if (b <= 0) {
        return "Ошибка: b должно быть положительным числом.";
    }
    
    const remainder = a % b;

    if (remainder === c || remainder === d) {
        return "Да, остаток равен одному из заданных чисел.";
    } else {
        return "Нет, остаток не равен ни одному из заданных чисел.";
    }
}

try {
    let a = parseInt(prompt("Введите неотрицательное целое число a:"), 10);
    let b = parseFloat(prompt("Введите положительное число b:"));
    let c = parseInt(prompt("Введите число c:"));
    let d = parseInt(prompt("Введите число d:"));

    if (!isNaN(a) && a >= 0 && Number.isInteger(a) && 
        !isNaN(b) && b > 0 && 
        !isNaN(c) && Number.isInteger(c) && 
        !isNaN(d) && Number.isInteger(d)) {
        
        let result = checkRemainder(a, b, c, d);
        console.log(result);
    } else {
        throw new Error("Пожалуйста, введите корректные числа.");
    }
} catch (error) {
    console.error("Произошла ошибка:", error.message);
}