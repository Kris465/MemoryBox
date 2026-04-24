const prompt = require('prompt-sync')();


function calculateCuboidProperties(a, b, h) {
    const volume = a * b * h;
    const lateralSurfaceArea = 2 * h * (a + b);
    return { volume, lateralSurfaceArea };
}


const a = parseFloat(prompt("Введите длину первой стороны (a):"));
const b = parseFloat(prompt("Введите длину второй стороны (b):"));
const h = parseFloat(prompt("Введите длину третьей стороны (h):"));

const result = calculateCuboidProperties(a, b, h);

console.log(`Объем: ${result.volume}`);
console.log(`Площадь боковой поверхности: ${result.lateralSurfaceArea}`);