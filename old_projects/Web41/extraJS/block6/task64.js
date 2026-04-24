const prompt = require('prompt-sync')();  
const enginePowers = [150, 180, 210, 190, 220, 170, 200, 230, 160, 185,
                      195, 205, 175, 215, 185, 195, 225, 185, 195, 205,
                      210, 190, 180, 200, 215, 185, 195, 205, 225];

let hasPowerAbove200 = false;
for (let i = 0; i < enginePowers.length; i++) {
    if (enginePowers[i] > 200) {
        hasPowerAbove200 = true;
        break;
    }
}

if (hasPowerAbove200) {
    console.log("Среди моделей есть автомобиль с мощностью двигателя более 200 л. с.");
} else {
    console.log("Нет моделей с мощностью двигателя более 200 л. с.");
}