const prompt = require('prompt-sync')(); 

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Введите натуральное число: ', (input) => {
  const numStr = input.trim();
  if (!/^\d+$/.test(numStr)) {
    console.log('Пожалуйста, введите натуральное число.');
    rl.close();
    return;
  }
  rl.question('Введите значение a для суммы цифр: ', (aInput) => {
    const a = Number(aInput);
    rl.question('Введите значение b для произведения цифр: ', (bInput) => {
      const b = Number(bInput);
      rl.question('Введите число k для количества цифр: ', (kInput) => {
        const k = Number(kInput);
        rl.question('Введите значение m для сравнения с первой цифрой: ', (mInput) => {
          const m = Number(mInput);
          const digits = numStr.split('').map(Number);
          const firstDigit = digits[0];
          const lengthDigits = digits.length;
          const sumDigits = digits.reduce((sum, d) => sum + d, 0);
          const prodDigits = digits.reduce((prod, d) => prod * d, 1);
          
          const conditionA = sumDigits < a;
          const conditionB = prodDigits > b;
          const conditionC = lengthDigits === k;
          const conditionD = firstDigit > m;

          console.log(`а) Сумма цифр меньше ${a}? ${conditionA}`);
          console.log(`б) Произведение цифр больше ${b}? ${conditionB}`);
          console.log(`в) Число k-значное? ${conditionC}`);
          console.log(`г) Первая цифра превышает ${m}? ${conditionD}`);

          rl.close();
        });
      });
    });
  });
}); 