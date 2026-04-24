const prompt = require('prompt-sync')();

function isEquilateralTriangle(a, b, c) {
    return a === b && b === c; 
}

try {
    let a = parseFloat(prompt("Введите длину стороны a:"));
    let b = parseFloat(prompt("Введите длину стороны b:"));
    let c = parseFloat(prompt("Введите длину стороны c:"));

    if (!isNaN(a) && isFinite(a) && a > 0 && 
        !isNaN(b) && isFinite(b) && b > 0 && 
        !isNaN(c) && isFinite(c) && c > 0) {
        
        let result = isEquilateralTriangle(a, b, c);
        if (result) {
            console.log("Да, треугольник является равносторонним.");
        } else {
            console.log("Нет, треугольник не является равносторонним.");
        }
    } else {
        throw new Error("Пожалуйста, введите корректные положительные числа для сторон треугольника.");
    }
} catch (error) {
    console.error("Произошла ошибка:", error.message);
}