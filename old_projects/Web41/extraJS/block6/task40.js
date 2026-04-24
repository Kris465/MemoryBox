const prompt = require('prompt-sync')();

function getThirdDigitTwoLoops() {
  let n = prompt("Введите натуральное число больше 99:");
  n = Number(n);

  if (isNaN(n) || n <= 99 || !Number.isInteger(n)) {
    console.log("Пожалуйста, введите целое число больше 99.");
    return;
  }

  let temp = n;
  let firstDigit;

 
  while (temp >= 10) {
    temp = Math.floor(temp / 10);
  }
  firstDigit = temp;

 
  temp = n;
  while (temp >= 1000) {
    temp = Math.floor(temp /10);
  }


  const thirdDigit = Math.floor((temp %1000)/100);

  console.log(`Третья цифра числа ${n} — ${thirdDigit}`);
}

getThirdDigitTwoLoops();