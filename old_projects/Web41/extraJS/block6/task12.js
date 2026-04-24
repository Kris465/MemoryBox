const prompt = require('prompt-sync')();

const a = parseFloat(prompt("Введите число a (1 < a < 1.5):"));
if (a <= 1 || a >= 1.5) {
    alert("Число должно быть в диапазоне (1, 1.5).");
} else {
    let i = 2;
    while (true) {
        const currentNumber = 1 / i;
        if (currentNumber < a) {
            console.log(`Первое число вида 1/2, 1/3, ... меньшее чем ${a} — это ${currentNumber} = 1/${i}`);
            break;
        }
        i++;
    }
}