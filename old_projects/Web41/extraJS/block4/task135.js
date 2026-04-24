const prompt = require('prompt-sync')();

const t = parseFloat(prompt("Введите время в минутах с начала часа:"));

if (t < 0 || t >= 60) {
  console.log("Время должно быть от 0 до 60 минут.");
} else {
  const cycleTime = t % 9;

  if (cycleTime >= 0 && cycleTime < 3) {
    console.log("Зеленый");
  } else if (cycleTime >=3 && cycleTime <4) {
    console.log("Желтый");
  } else if (cycleTime >=4 && cycleTime <6) {
    console.log("Красный");
  } else {
    console.log("Зеленый");
  }
}