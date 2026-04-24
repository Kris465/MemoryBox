
const n = parseInt(prompt("Введите число от 1 до 9 для вывода таблицы умножения:"), 10);

if (isNaN(n) || n < 1 || n > 9) {
    console.log("Некорректный ввод. Пожалуйста, введите число от 1 до 9.");
} else {
    console.log(`Таблица умножения на ${n}:`);
    console.log("-------------------------");

    for (let i = 1; i <= 10; i++) {
        const result = n * i;
        console.log(`${n} x ${i} = ${result}`);
    }
}