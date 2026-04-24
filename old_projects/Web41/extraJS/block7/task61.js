const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите количество участников:"), 10);
const times = [];

for (let i = 0; i < n; i++) {
    const time = parseFloat(prompt(`Введите время участника ${i + 1}:`));
    times.push({ order: i + 1, time: time });
}

let bestTime = times[0];

for (let i = 1; i < n; i++) {
    if (times[i].time < bestTime.time) {
        bestTime = times[i];
    }
}

console.log(`Лучший результат показал спортсмен №${bestTime.order}`);