const prompt = require('prompt-sync')();


function calculateTriangleArea(x1, y1, x2, y2, x3, y3) {
    // Вычисляем площадь треугольника по координатам вершин
    return Math.abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2);
}

function calculateQuadrilateralArea(x1, y1, x2, y2, x3, y3, x4, y4) {
    // Разбиваем четырехугольник на два треугольника:
    // 1. Треугольник 1: вершины (x1, y1), (x2, y2), (x3, y3)
    // 2. Треугольник 2: вершины (x1, y1), (x3, y3), (x4, y4)
    const area1 = calculateTriangleArea(x1, y1, x2, y2, x3, y3);
    const area2 = calculateTriangleArea(x1, y1, x3, y3, x4, y4);

    // Суммируем площади треугольников
    return area1 + area2;
}

// Запрашиваем координаты у пользователя
const x1 = parseFloat(prompt("Введите x-координату первой вершины:"));
const y1 = parseFloat(prompt("Введите y-координату первой вершины:"));
const x2 = parseFloat(prompt("Введите x-координату второй вершины:"));
const y2 = parseFloat(prompt("Введите y-координату второй вершины:"));
const x3 = parseFloat(prompt("Введите x-координату третьей вершины:"));
const y3 = parseFloat(prompt("Введите y-координату третьей вершины:"));
const x4 = parseFloat(prompt("Введите x-координату четвертой вершины:"));
const y4 = parseFloat(prompt("Введите y-координату четвертой вершины:"));

// Вычисляем площадь четырехугольника
const area = calculateQuadrilateralArea(x1, y1, x2, y2, x3, y3, x4, y4);

// Выводим результат
console.log("Площадь четырехугольника:", area);