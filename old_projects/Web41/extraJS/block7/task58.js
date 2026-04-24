const n = parseInt(prompt("Введите количество кругов:"), 10);
const areas = [];

for (let i = 0; i < n; i++) {
    const area = parseFloat(prompt(`Введите площадь круга ${i + 1}:`));
    areas.push(area);
}

let minArea = areas[0];

for (let i = 1; i < n; i++) {
    if (areas[i] < minArea) {
        minArea = areas[i];
    }
}

const radius = Math.sqrt(minArea / Math.PI);

console.log(`Радиус самого маленького круга: ${radius}`);