const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите количество учеников:"), 10);
let countFives = 0;
for (let i = 0; i < n; i++) {
    const grade = parseInt(prompt(`Введите оценку ученика ${i + 1}:`), 10);
    if (grade === 5) {
        countFives++;
    }
}
console.log("Количество пятёрок:", countFives);