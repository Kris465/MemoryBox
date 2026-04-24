
function f(x) {
    if (x > 2.4 && x < 5.7) {
        return x * x; 
    } else {
        return 4; 
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