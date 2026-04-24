const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите количество людей:"), 10);
const masses = [];

for (let i = 0; i < n; i++) {
    masses.push(parseFloat(prompt(`Введите массу человека ${i + 1} (кг):`)));
}

const fullPeople = masses.filter(mass => mass > 100);
const others = masses.filter(mass => mass <= 100);

const sumFull = fullPeople.reduce((sum, mass) => sum + mass, 0);
const sumOthers = others.reduce((sum, mass) => sum + mass, 0);

const avgFull = sumFull / fullPeople.length;
const avgOthers = others.length > 0 ? sumOthers / others.length : 0;

console.log("Средняя масса полных людей:", avgFull);
console.log("Средняя масса остальных людей:", avgOthers);