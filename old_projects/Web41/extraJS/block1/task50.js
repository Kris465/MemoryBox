const prompt = require('prompt-sync')();

function calculateDistance(x1, y1, x2, y2) {
    return Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
}

function calculateTrianglePerimeterAndArea(x1, y1, x2, y2, x3, y3) {
    const a = calculateDistance(x1, y1, x2, y2);
    const b = calculateDistance(x2, y2, x3, y3); 
    const c = calculateDistance(x1, y1, x3, y3); 

    const perimeter = a + b + c;

    const s = perimeter / 2;
    const area = Math.sqrt(s * (s - a) * (s - b) * (s - c));

    return { perimeter, area };
}

const x1 = parseFloat(prompt("Введите x-координату первой вершины (A):"));
const y1 = parseFloat(prompt("Введите y-координату первой вершины (A):"));
const x2 = parseFloat(prompt("Введите x-координату второй вершины (B):"));
const y2 = parseFloat(prompt("Введите y-координату второй вершины (B):"));
const x3 = parseFloat(prompt("Введите x-координату третьей вершины (C):"));
const y3 = parseFloat(prompt("Введите y-координату третьей вершины (C):"));

const result = calculateTrianglePerimeterAndArea(x1, y1, x2, y2, x3, y3);

console.log("Периметр треугольника:", result.perimeter);
console.log("Площадь треугольника:", result.area);