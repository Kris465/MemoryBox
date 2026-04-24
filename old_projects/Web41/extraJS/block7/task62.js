const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите количество команд:"), 10);
const points = [];

for (let i = 0; i < n; i++) {
    const score = parseInt(prompt(`Введите очки команды ${i + 1}:`), 10);
    points.push({ number: i + 1, score: score });
}

let minPoints = points[0];

for (let i = 1; i < n; i++) {
    if (points[i].score < minPoints.score) {
        minPoints = points[i];
    }
}

console.log(`Номер команды с наименьшим количеством очков: ${minPoints.number}`);