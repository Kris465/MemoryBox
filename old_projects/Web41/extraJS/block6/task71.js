const prompt = require('prompt-sync')(); 

const heights = [];
const n = parseInt(prompt("Введите количество учащихся:"), 10);
for (let i = 0; i < n; i++) {
    const height = parseFloat(prompt(`Введите рост ученика ${i + 1}:`));
    heights.push(height);
}

let isDescending = true;
for (let i = 0; i < heights.length - 1; i++) {
    if (heights[i] < heights[i + 1]) {
        isDescending = false;
        break;
    }
}

if (isDescending) {
    console.log("Ученики перечислены в порядке убывания роста.");
} else {
    console.log("Ученики не перечислены в порядке убывания роста.");
}