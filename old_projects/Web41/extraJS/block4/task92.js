const prompt = require('prompt-sync')();
function determineRegion(x, y) {
    if (x > 0 && y > 0) {
        return "I"; 
    } else if (x < 0 && y > 0) {
        return "II"; 
    } else if (x < 0 && y < 0) {
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