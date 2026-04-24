const prompt = require('prompt-sync')();

// Ввод количества учеников
const n = parseInt(prompt("Введите количество учеников:"), 10);
const heights = [];

// Ввод роста каждого ученика
for (let i = 0; i < n; i++) {
    heights.push(parseFloat(prompt(`Введите рост ученика ${i + 1} (отрицательное для мальчиков, положительное для девочек):`)));
}

// Разделение по полу
const boys = heights.filter(height => height < 0);
const girls = heights.filter(height => height > 0);

// Вычисление суммы для каждой группы
const sumBoys = boys.reduce((sum, height) => sum + height, 0);
const sumGirls = girls.reduce((sum, height) => sum + height, 0);

// Вычисление среднего роста
const avgBoys = boys.length > 0 ? sumBoys / boys.length : 0;
const avgGirls = girls.length > 0 ? sumGirls / girls.length : 0;

// Вывод результатов
console.log("Средний рост мальчиков:", avgBoys);
console.log("Средний рост девочек:", avgGirls);