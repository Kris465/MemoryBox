const n = parseFloat(prompt("Введите число n:"));
const f = parseFloat(prompt("Введите первый член прогрессии f:"));
const s = parseFloat(prompt("Введите шаг s:"));

const isMember = (n - f) % s === 0 && (n - f) / s >= 0;

console.log(`Число ${n} ${isMember ? "является" : "не является"} членом арифметической прогрессии с первым членом ${f} и шагом ${s}.`);