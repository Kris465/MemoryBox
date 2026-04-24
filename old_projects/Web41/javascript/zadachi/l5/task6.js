const prompt = require('prompt-sync')();

function left(n) {
    if (n < 10) {
        return n.toString();
    } else {
        return (n % 10).toString() + left(Math.floor(n / 10));
    }
}

let chislo = prompt('Введите число: ');
const result = left(chislo);

console.log(result);
