const prompt = require('prompt-sync')();

function swapFirstTwoDigits(number) {
  const numStr = number.toString();

  if (numStr.length !== 3) {
    return "Ошибка: Число должно быть трехзначным.";
  }

  const digit1 = numStr[0];
  const digit2 = numStr[1];
  const digit3 = numStr[2];

  const newNumStr = digit2 + digit1 + digit3;
  const newNumber = parseInt(newNumStr, 10);

  return newNumber;
}

const numberStr = prompt("Введите трехзначное число: ");
const number = parseInt(numberStr);

if (isNaN(number)) {
  console.log("Ошибка: Введите число.");
} else {
  const newNumber = swapFirstTwoDigits(number);
  if (typeof newNumber === 'string') {
      console.log(newNumber);
  } else {
      console.log(`Исходное число: ${number}, Новое число: ${newNumber}`);
  }
}