const prompt = require('prompt-sync')();


let y = parseFloat(prompt("Введите угол поворота часовой стрелки (0 < y <= 2): "));


if (y <= 0 || y > 2) {
    console.log("Некорректный угол. Пожалуйста, введите значение в диапазоне от 0 до 2.");
} else {

    let hours = Math.floor(y * 12); 
    let remainingAngle = (y * 12 - hours) * 30;
    let minutes = Math.floor((remainingAngle / 30) * 60); 


    let minuteAngle = minutes * 6;
  
    console.log(`Угол минутной стрелки: ${minuteAngle} градусов`);
    console.log(`С начала суток прошло: ${hours} полных часов и ${minutes} полных минут.`);
}