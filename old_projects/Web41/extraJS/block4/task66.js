const prompt = require('prompt-sync')();

function maxDominoes(a, b, c, d, e) {
    // Проверяем, что размеры стола и костей корректны
    if (a <= 0 || b <= 0 || c <= d || d <= e) {
        return 0;
    }

    // Количество костей в горизонтальном положении
    const horizontalCount = Math.floor(a / c) * Math.floor(b / d) +
                            Math.floor(a / d) * Math.floor(b / c);

    // Количество костей в вертикальном положении
    const verticalCount = Math.floor(a / c) * Math.floor(b / e) +
                          Math.floor(a / e) * Math.floor(b / c) +
                          Math.floor(a / d) * Math.floor(b / e) +
                          Math.floor(a / e) * Math.floor(b / d);

    // Возвращаем максимальное количество костей
    return Math.max(horizontalCount, verticalCount);
}

// Пример использования
const a = 10; // Длина стола
const b = 5;  // Ширина стола
const c = 3;  // Длина кости
const d = 2;  // Ширина кости
const e = 1;  // Высота кости

const result = maxDominoes(a, b, c, d, e);
console.log(`Максимальное количество костей домино, которое можно разместить: ${result}`);