const prompt = require('prompt-sync')();
const n = parseInt(prompt("Введите длину последовательности n:"), 10);
const sequence = [];

for (let i = 0; i < n; i++) {
    const num = parseInt(prompt(`Введите число ${i + 1}:`), 10);
    sequence.push(num);
}

// Подсчет количества изменений знака
let signChanges = 0;

for (let i = 0; i < n - 1; i++) {
    // Проверяем, что оба числа ненулевые (по условию)
    if (sequence[i] * sequence[i + 1] < 0) {
        signChanges++;
    }
}

// Вывод результата
console.log(`Количество изменений знака: ${signChanges}`);