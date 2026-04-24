const prompt = require('prompt-sync')();

function determineRegion(x, y) {
    if (y > 5) {
        return "I"; 
    } else if (y > 2.5 && y <= 5) {
        return "II"; 
    } else if (y <= 2.5) {
        return "III";
    } else {
        return "Точка на границе областей";
    }
}

const inputX = parseFloat(prompt("Введите координату x:"));
const inputY = parseFloat(prompt("Введите координату y:"));

if (!isNaN(inputX) && !isNaN(inputY)) {
    const region = determineRegion(inputX, inputY); 
    console.log(`Точка с координатами (${inputX}, ${inputY}) попадает в область: ${region}`);
} else {
    console.log("Пожалуйста, введите корректные числовые значения для координат.");
}