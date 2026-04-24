const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Введите натуральное число, все цифры которого различны: ', (input) => {
  const nStr = input.trim();

  if (!/^\d+$/.test(nStr)) {
    console.log('Некорректный ввод.');
    rl.close();
    return;
  }

  const digits = nStr.split('').map(Number);
  const len = digits.length;

  let maxDigit = -1, minDigit = 10;
  let maxPosStart = -1, maxPosEnd = -1;
  let minPosStart = -1, minPosEnd = -1;

  for (let i = 0; i < len; i++) {
    const d = digits[i];
    if (d > maxDigit) {
      maxDigit = d;
      maxPosStart = i + 1;
      maxPosEnd = len - i;
    }
    if (d < minDigit) {
      minDigit = d;
      minPosStart = i + 1;
      minPosEnd = len - i;
    }
  }

  console.log(`Порядковый номер двух максимальных цифр: от начала — ${maxPosStart}, от конца — ${maxPosEnd}`);
  console.log(`Порядковый номер двух минимальных цифр: от начала — ${minPosStart}, от конца — ${minPosEnd}`);

  rl.close();
});