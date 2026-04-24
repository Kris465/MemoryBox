const prompt = require('prompt-sync')(); 

const width = 425;
const height = 131;

let w = width;
let h = height;
const squares = [];

while (w >= h && h > 0) {
    const count = Math.floor(w / h);
    squares.push({ side: h, count: count });
    w = w % h;
    if (w < h) {
        [w, h] = [h, w];
    }
}

console.log("Квадраты и их количество:");
squares.forEach((square) => {
    console.log(`Квадрат со стороной ${square.side}: ${square.count} шт.`);
});