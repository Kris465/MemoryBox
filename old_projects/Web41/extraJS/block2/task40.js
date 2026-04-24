const prompt = require('prompt-sync')();

let y = parseFloat(prompt("Введите угол поворота часовой стрелки (0 <= y < 360): "));

if (y < 0 || y >= 360) {
    console.log("Некорректный угол. Пожалуйста, введите значение в диапазоне от 0 до 360.");
} else {
    let hours = Math.floor(y / 30); 

    let remainingAngle = y % 30;

    let minutes = Math.floor((remainingAngle / 30) * 60); 

    console.log(`С начала суток прошло: ${hours} полных часов и ${minutes} полных минут.`);
}