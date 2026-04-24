const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите количество квартир:"), 10);
const residents = [];

for (let i = 1; i <= n; i++) {
    const count = parseInt(prompt(`Введите количество жильцов в квартире №${i}:`), 10);
    residents.push({ number: i, count: count });
}

let maxResidents = residents[0];

for (let i = 1; i < n; i++) {
    if (residents[i].count > maxResidents.count || 
       (residents[i].count === maxResidents.count && residents[i].number > maxResidents.number)) {
        maxResidents = residents[i];
    }
}

console.log(`Квартира с максимальным числом жильцов: №${maxResidents.number} (${maxResidents.count} жильцов)`);