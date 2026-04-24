const prompt = require('prompt-sync')();

let h = parseInt(prompt("Введите часы (0 <= h <= 23): "));
let m = parseInt(prompt("Введите минуты (0 <= m <= 59): "));
let s = parseInt(prompt("Введите секунды (0 <= s <= 59): "));

if (h < 0 || h > 23 || m < 0 || m > 59 || s < 0 || s > 59) {
    console.log("Некорректное время. Пожалуйста, введите значения в допустимом диапазоне.");
} else {

    h = h % 12;


    let hourAngle = (h * 30) + (m * 0.5) + (s * (0.5 / 60)); 
    let minuteAngle = m * 6 + (s * 0.1);

 
    let angle = Math.abs(hourAngle - minuteAngle);

    if (angle > 180) {
        angle = 360 - angle;
    }

    console.log(`Угол между часовой стрелкой и положением 12 часов: ${angle} градусов`);
}