const prompt = require('prompt-sync')();

const a = parseFloat(prompt("Введите число a (1 <= a <= 1.5):"));
if (a < 1 || a > 1.5) {
    alert("Число должно быть в диапазоне [1, 1.5].");
} else {
    let n = 1;
    while (true) {
        let allGreaterOrEqualA = true;
        for (let i = 2; i <= n + 1; i++) {
            if (1 + 1 / i < a) {
                allGreaterOrEqualA = false;
                break;
            }
        }
        if (!allGreaterOrEqualA) {
            break;
        }
        console.log(n);
        n++;
    }
}