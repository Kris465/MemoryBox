const prompt = require('prompt-sync')();

const num = parseInt(prompt("Введите число для вывода:"), 10);
const count = parseInt(prompt("Сколько раз вывести это число?"), 10);

if (isNaN(num) || isNaN(count) || count <= 0) {
  console.log("Некорректный ввод");
} else {
  for (let i = 0; i < count; i++) {
    console.log(num);
  }
}