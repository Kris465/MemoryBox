
function isPointInShadedArea(x, y) {
    let conditionA = (y >= 0 && y <= 2 && x >= 0 && x <= 1); 
    let conditionB = (y >= 0 && y <= 4 && x >= 0 && x <= 2); 
    let conditionC = (y >= 1.5 && y <= 2 && x >= 1 && x <= 2); 
    let conditionD = (y >= 0 && y <= 1 && x >= -1 && x <= 1);
    let conditionE = (y >= 1.5 && y <= 3 && x >= 0.5 && x <= 2); 

    return conditionA || conditionB || conditionC || conditionD || conditionE;
}

let x = parseFloat(prompt("Введите координату x:"));
let y = parseFloat(prompt("Введите координату y:"));

if (isPointInShadedArea(x, y)) {
    console.log(`Точка (${x}, ${y}) попадает в заштрихованные области.`);
} else {
    console.log(`Точка (${x}, ${y}) не попадает в заштрихованные области.`);
}