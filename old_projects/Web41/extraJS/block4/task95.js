const prompt = require('prompt-sync')();

function determineWeightCategory(weight) {
    if (weight < 60) {
        return "Легкий вес"; 
    } else if (weight < 64) {
        return "Первый полусредний вес"; 
    } else if (weight < 69) {
        return "Полусредний вес"; 
    } else {
        return "Вес не соответствует ни одной категории"; 
    }
}


const inputWeight = parseFloat(prompt("Введите вес боксера (в кг):"));


if (!isNaN(inputWeight)) {
    const category = determineWeightCategory(inputWeight); 
    console.log(`Боксер с весом ${inputWeight} кг относится к категории: ${category}`); 
} else {
    console.log("Пожалуйста, введите корректное числовое значение для веса."); 
}