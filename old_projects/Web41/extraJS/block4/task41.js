const prompt = require('prompt-sync')();

function f(x) {
    if (x > 0.2 && x < 0.9) {
        return x * Math.sin(x); 
    } else {
        return 1; 
    }
}
try {
    let x = parseFloat(prompt("Введите вещественное число x:"));

    if (!isNaN(x) && isFinite(x)) {
        let result = f(x);
        console.log(`f(${x}) = ${result}`);
    } else {
        throw new Error("Пожалуйста, введите корректное вещественное число.");
    }
} catch (error) {
    console.error("Произошла ошибка:", error.message);
}