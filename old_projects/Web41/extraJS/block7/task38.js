const prompt = require('prompt-sync')();
const n = parseInt(prompt("Введите количество троек n:"), 10);
let count = 0;

for (let i = 0; i < n; i++) {

    const a = parseInt(prompt(`Введите a для тройки ${i + 1}:`), 10);
    const b = parseInt(prompt(`Введите b для тройки ${i + 1}:`), 10);
    const c = parseInt(prompt(`Введите c для тройки ${i + 1}:`), 10);


    if (!(a <= b && b <= c)) {
        alert(`Тройка должна быть отсортирована: a ≤ b ≤ c. Попробуйте снова.`);
        i--;
        continue;
    }


    if (c < a + b) {
        count++;
    }
}


console.log(`Количество троек, которые могут образовать треугольник: ${count}`);