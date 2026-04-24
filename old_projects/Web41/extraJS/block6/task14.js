const prompt = require('prompt-sync')();

const a = parseFloat(prompt("Введите число a (1 < a < 1.5):"));
if (a <= 1 || a >= 1.5) {
    alert("Число должно быть в диапазоне (1, 1.5).");
} else {
    let n = 1;
    while (true) {
        const current = 1 + 1 / n;
        if (current < a) {
            console.log(n);
            break;
        }
        n++;
    }
}