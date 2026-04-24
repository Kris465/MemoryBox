const prompt = require('prompt-sync')();

function getQuadrant(x, y) {
    if (x > 0 && y > 0) {
        return "Первая четверть";
    } else if (x < 0 && y > 0) {
        return "Вторая четверть";
    } else if (x < 0 && y < 0) {
        return "Третья четверть";
    } else if (x > 0 && y < 0) {
        return "Четвертая четверть";
    } else {
        return "Координаты не должны быть равны нулю.";
    }
}

const x = parseFloat(prompt("Введите первое число не равное 0:"));
const y = parseFloat(prompt("Введите второе число не равное 0:"));

const quadrant = getQuadrant(x, y);
console.log("Точка находится в:", quadrant);