function secondDigitTwoLoops(n) {
  let temp = n;
  let firstDigit = null;
  let secondDigit = null;

  while (temp >= 10) {
    temp = Math.floor(temp / 10);
  }
  firstDigit = temp;

  temp = n;
  while (temp >= 100) {
    temp = Math.floor(temp / 10);
  }
  secondDigit = temp % 10;

  return secondDigit;
}

const n1 = 12345;
console.log(`Вторая цифра числа ${n1} — ${secondDigitTwoLoops(n1)}`);