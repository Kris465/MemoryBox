const prompt = require('prompt-sync')();

const a = parseFloat(prompt("Введите число a (1 < a < 1.5):"));

if (a <= 1 || a >= 1.5) {
    alert("Число должно быть в диапазоне (1, 1.5).");
} else {
    let i = 1;
    while (true) {
        const value = 1 / i;
        if (value < a) {
            break; 
        }
        console.log(`1/${i} = ${value}`);
        i++;
    }
}