const prompt = require('prompt-sync')();  

function isInArea(x, y) {
    return (x > 0 && y > 0) || (x < 0 && y < 0);
}

try {
    let x = parseFloat(prompt("Введите координату x:"));
    let y = parseFloat(prompt("Введите координату y:"));

    if (!isNaN(x) && isFinite(x) && !isNaN(y) && isFinite(y)) {
        if (isInArea(x, y)) {
            console.log(`Точка (${x}, ${y}) попадает в одну из областей I или III.`);
        } else {
            console.log(`Точка (${x}, ${y}) не попадает в области I или III.`);
        }
    } else {
        throw new Error("Пожалуйста, введите корректные числа.");
    }
} catch (error) {
    console.error("Произошла ошибка:", error.message);
}