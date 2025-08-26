const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите количество городов:"), 10);
const distances = [];

for (let i = 0; i < n; i++) {
    const distance = parseFloat(prompt(`Введите расстояние от Москвы до города ${i + 1}:`));
    distances.push(distance);
}

let maxDistance = distances[0];

for (let i = 1; i < n; i++) {
    if (distances[i] > maxDistance) {
        maxDistance = distances[i];
    }
}

console.log(`Самое удаленное от Москвы расстояние: ${maxDistance}`);