const a = parseInt(prompt("Введите длину прямоугольника a:"), 10);
const b = parseInt(prompt("Введите ширину прямоугольника b:"), 10);

let w = a;
let h = b;
const squares = [];

while (w > 0 && h > 0) {
    const side = Math.min(w, h);
    const count = Math.floor(w / side) * Math.floor(h / side);
    squares.push({ side: side, count: count });
    if (w > h) {
        w = w % h;
    } else {
        h = h % w;
    }
}

console.log("Квадраты и их количество:");
squares.forEach((square) => {
    console.log(`Квадрат со стороной ${square.side}: ${square.count} шт.`);
});