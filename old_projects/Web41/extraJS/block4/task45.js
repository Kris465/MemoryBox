
function hasEqualPair(a, b, c) {
    return a === b || a === c || b === c; 
}

try {
    let a = parseFloat(prompt("Введите вещественное число a:"));
    let b = parseFloat(prompt("Введите вещественное число b:"));
    let c = parseFloat(prompt("Введите вещественное число c:"));

    if (!isNaN(a) && isFinite(a) && !isNaN(b) && isFinite(b) && !isNaN(c) && isFinite(c)) {
        let result = hasEqualPair(a, b, c);
        if (result) {
            console.log("Да, имеется хотя бы одна пара равных между собой чисел.");
        } else {
            console.log("Нет, среди чисел нет равных между собой.");
        }
    } else {
        throw new Error("Пожалуйста, введите корректные вещественные числа.");
    }
} catch (error) {
    console.error("Произошла ошибка:", error.message);
}