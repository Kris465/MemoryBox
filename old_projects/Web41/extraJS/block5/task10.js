const prompt = require('prompt-sync')();

const exchangeRate = parseFloat(prompt("Введите текущий курс доллара к рублю:"));

if (isNaN(exchangeRate) || exchangeRate <= 0) {
    console.log("Некорректный ввод курса. Пожалуйста, введите положительное число.");
} else {
    console.log("Доллары США | Рубли");
    console.log("---------------------");

    for (let dollars = 1; dollars <= 20; dollars++) {
        const rubles = (dollars * exchangeRate).toFixed(2);
        console.log(`${dollars}           | ${rubles}`);
    }
}