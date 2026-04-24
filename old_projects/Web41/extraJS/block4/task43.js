const prompt = require('prompt-sync')();

function checkDivisibility(a, b) {
    if (b !== 0 && a % b === 0) {
        return "Да, одно из чисел является делителем другого"; 
    } else if (a !== 0 && b % a === 0) {
        return "Да, одно из чисел является делителем другого"; 
    } else {
        return "Нет, ни одно из чисел не является делителем другого"; 
    }
}


try {
    let a = parseFloat(prompt("Введите число a:"));
    let b = parseFloat(prompt("Введите число b:"));

    if (!isNaN(a) && isFinite(a) && !isNaN(b) && isFinite(b)) {
        let result = checkDivisibility(a, b);
        console.log(result);
    } else {
        throw new Error("Пожалуйста, введите корректные числа.");
    }
} catch (error) {
    console.error("Произошла ошибка:", error.message);
}