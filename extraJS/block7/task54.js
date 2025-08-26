const prompt = require('prompt-sync')();

// Ввод данных
const n = parseInt(prompt("Введите n:"));
const inputStr = prompt(`Введите ${n} целых чисел через пробел:`);
const a = inputStr.trim().split(' ').map(Number);

// Проверка правильности ввода
if (a.length !== n) {
  alert("Количество введённых чисел не совпадает с n");
} else {
  let maxValue = a[0];
  let minValue = a[0];
  let maxIndex = 0; // индекс последнего максимума
  let minIndex = 0; // индекс последнего минимума

  for (let i = 0; i < n; i++) {
    // Обновляем последний индекс максимума при равенстве или большем значении
    if (a[i] >= maxValue) {
      maxValue = a[i];
      maxIndex = i;
    }
    // Обновляем последний индекс минимума при меньшем значении
    if (a[i] <= minValue) {
      minValue = a[i];
      minIndex = i;
    }
  }

  // Вывод номеров (нумерация с 1)
  console.log("Номер последнего максимального элемента:", maxIndex + 1);
  console.log("Номер последнего минимального элемента:", minIndex + 1);
}