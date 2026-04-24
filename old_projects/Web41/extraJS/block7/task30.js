const prompt = require('prompt-sync')();

const birthYears = [1980, 1987, 1992, 1975, 1983, 1995, 1988]; // пример данных

let bornBefore1985 = 0;
let bornAfter1990 = 0;

for (let year of birthYears) {
    if (year < 1985) {
        bornBefore1985++;
    }
    if (year > 1990) {
        bornAfter1990++;
    }
}

console.log(`Людей, родившихся до 1985 года: ${bornBefore1985}`);
console.log(`Людей, родившихся после 1990 года: ${bornAfter1990}`);