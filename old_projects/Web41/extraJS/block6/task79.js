const prompt = require('prompt-sync')(); 

const m = parseFloat(prompt("Введите число m:"));
const g = parseFloat(prompt("Введите первый член прогрессии g:"));
const z = parseFloat(prompt("Введите знаменатель z:"));

let isMember = false;

if (z !== 0 && g !== 0) {
    if (m === g) {
        isMember = true;
    } else if ((m / g) > 0 && Math.abs((m / g) - Math.pow(z, Math.round(Math.log(m / g) / Math.log(z)))) < 1e-10) {
        isMember = true;
    }
} else if (g === 0 && m === 0) {
    isMember = true;
}

console.log(`Число ${m} ${isMember ? "является" : "не является"} членом геометрической прогрессии с первым членом ${g} и знаменателем ${z}.`);