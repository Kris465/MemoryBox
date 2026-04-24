const prompt = require('prompt-sync')();
const multiplesOf13 = [];

for (let i = 1; i < 100; i++) {
    if (i % 13 === 0) {
        multiplesOf13.push(i);
    }
}

console.log("Кратные 13 числа, меньшие 100:", multiplesOf13);