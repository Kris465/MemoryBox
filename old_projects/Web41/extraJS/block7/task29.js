const prompt = require('prompt-sync')();

const grades = [5, 3, 2, 4, 5, 2, 3, 5, 2, 4];

let fiveCount = 0;
let twoCount = 0;

for (let grade of grades) {
    if (grade === 5) {
        fiveCount++;
    } else if (grade === 2) {
        twoCount++;
    }
}

console.log(`Количество пятёрок: ${fiveCount}`);
console.log(`Количество двоек: ${twoCount}`);