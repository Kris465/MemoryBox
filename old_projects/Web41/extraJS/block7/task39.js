const prompt = require('prompt-sync')();

const g = 9.8; 

const n = parseInt(prompt("Введите количество целей n:"), 10);
const results = [];

const v0 = parseFloat(prompt("Введите начальную скорость v0:"), 10);

for (let i = 0; i < n; i++) {
    const R = parseFloat(prompt(`Введите расстояние R для цели ${i + 1}:`));
    const H = parseFloat(prompt(`Введите высоту H для цели ${i + 1}:`));

    const A = (g * R * R) / (2 * v0 * v0);

    const a_coef = A;
    const b_coef = -R;
    const c_coef = A + H;

    const D = b_coef * b_coef - 4 * a_coef * c_coef;

    if (D < 0) {
        results.push(false);
    } else {
        
        const sqrtD = Math.sqrt(D);
        const T1 = (-b_coef + sqrtD) / (2 * a_coef);
        const T2 = (-b_coef - sqrtD) / (2 * a_coef);

        const canHit =
            ((T1 >= 0 && isFinite(T1)) || (T2 >= 0 && isFinite(T2)));

        results.push(canHit);
    }
}

const hitsCount = results.filter(Boolean).length;
const percentHit = (hitsCount / n) * 100;

console.log(`Процент попаданий: ${percentHit.toFixed(2)}%`);