const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите количество оценок судей:"), 10);
const scores = [];

for (let i = 0; i < n; i++) {
    scores.push(parseFloat(prompt(`Введите оценку судьи ${i + 1}:`)));
}

let maxScore = Math.max(...scores);
let minScore = Math.min(...scores);

let maxIndex = scores.indexOf(maxScore);
let minIndex = scores.indexOf(minScore);

scores.splice(maxIndex, 1);
if (minIndex > maxIndex) {
    minIndex--;
}
scores.splice(minIndex, 1);

const sum = scores.reduce((acc, val) => acc + val, 0);
const result = sum / scores.length;

console.log(`Оценка, которая пойдет в зачет: ${result}`);