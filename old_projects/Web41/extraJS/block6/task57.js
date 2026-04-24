const prompt = require('prompt-sync')(); 

const sequence = [1.2, 2.5, 3.7, 4.8, 5.9, 6.1, 7.3, 8.4, 9.6, 10.7, 11.8, 12.9, 13.0, 14.2, 15.3];
const n = parseFloat(prompt("Введите число n (такое, что a1 < n < a15):"));

if (isNaN(n) || n <= sequence[0] || n >= sequence[sequence.length -1]) {
    console.log("Некорректное значение n");
} else {
    let minDiff = Infinity;
    let closestIndex = -1;
    for (let i = 0; i < sequence.length; i++) {
        const diff = Math.abs(sequence[i] - n);
        if (diff < minDiff) {
            minDiff = diff;
            closestIndex = i;
        }
    }
    console.log(`Ближайший к n элемент: порядковый номер ${closestIndex + 1}, значение ${sequence[closestIndex]}`);
}