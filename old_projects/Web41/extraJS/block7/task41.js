const prompt = require('prompt-sync')();

const grades = [5, 4, 3, 2, 5, 4, 3, 2, 5, 4]; 

let fives = 0;
let fours = 0;
let threes = 0;
let twos = 0;

for (let grade of grades) {
    if (grade === 5) {
        fives++;
    } else if (grade === 4) {
        fours++;
    } else if (grade === 3) {
        threes++;
    } else if (grade === 2) {
        twos++;
    }
}

console.log(`Пятерок: ${fives}`);
console.log(`Четверок: ${fours}`);
console.log(`Троек: ${threes}`);
console.log(`Двоек: ${twos}`);