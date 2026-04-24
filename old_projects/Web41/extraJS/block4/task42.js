const prompt = require('prompt-sync')();

function checkInequalities(a, b, c) {
    const inequality1 = a < b && b < c; 
    const inequality2 = b > a && a > c; 

    return { inequality1, inequality2 };
}


try {
    let a = parseFloat(prompt("Введите вещественное число a:"));
    let b = parseFloat(prompt("Введите вещественное число b:"));
    let c = parseFloat(prompt("Введите вещественное число c:"));

    if (!isNaN(a) && isFinite(a) && !isNaN(b) && isFinite(b) && !isNaN(c) && isFinite(c)) {
        const { inequality1, inequality2 } = checkInequalities(a, b, c);
        
        console.log(`Неравенство a < b < c: ${inequality1}`);
        console.log(`Неравенство b > a > c: ${inequality2}`);
    } else {
        throw new Error("Пожалуйста, введите корректные вещественные числа.");
    }
} catch (error) {
    console.error("Произошла ошибка:", error.message);
}