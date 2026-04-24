const prompt = require('prompt-sync')();

const a = parseInt(prompt("Введите номер первой квартиры (a):"), 10);
const n = parseInt(prompt("Введите количество квартир (n):"), 10);

if (isNaN(a) || isNaN(n) || n <= 0) {
  console.log("Некорректный ввод");
} else {
  let sum = 0;
  for (let i = 0; i < n; i++) {
    sum += a + i;
  }

  if (sum % 2 === 0) {
    console.log("Сумма номеров всех квартир является четным числом.");
  } else {
    console.log("Сумма номеров всех квартир является нечетным числом.");
  }
}