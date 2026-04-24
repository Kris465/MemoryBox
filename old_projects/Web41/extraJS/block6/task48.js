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
  rl.question('Введите значение k для суммы цифр: ', (kInput) => {
    const k = Number(kInput);
    rl.question('Введите значение b для сравнения числа: ', (bInput) => {
      const b = Number(bInput);
      rl.question('Введите цифру x для начала числа: ', (xInput) => {
        const x = Number(xInput);
        rl.question('Введите цифру y для конца числа: ', (yInput) => {
          const y = Number(yInput);
          rl.question('Введите значение a для произведения цифр: ', (aInput) => {
            const a = Number(aInput);
            rl.question('Введите значение m для суммы цифр: ', (mInput) => {
              const m = Number(mInput);
              rl.question('Введите значение n для делимости: ', (nInput) => {
                const n = Number(nInput);

                const digits = numStr.split('').map(Number);
                const firstDigit = digits[0];
                const lastDigit = digits[digits.length -1];
                const lengthDigits = digits.length;
                const sumDigits = digits.reduce((sum, d) => sum + d, 0);
                const prodDigits = digits.reduce((prod, d) => prod * d, 1);
                const numValue = Number(numStr);

                const conditionA = (sumDigits > k) && (numValue % 2 ===0);
                const conditionB = (lengthDigits %2 ===0) && (numValue <= b);
                const conditionC = (firstDigit === x) && (lastDigit === y);
                const conditionD = (prodDigits < a) && (numValue % n ===0);
                const conditionE = (sumDigits > m) && (numValue % n ===0);

                console.log(`а) Сумма цифр больше ${k} и число четное? ${conditionA}`);
                console.log(`б) Количество цифр четное и число не превышает ${b}? ${conditionB}`);
                console.log(`в) Начинается цифрой ${x} и заканчивается цифрой ${y}? ${conditionC}`);
                console.log(`г) Произведение цифр меньше ${a} и число делится на ${b}? ${conditionD}`);
                console.log(`д) Сумма цифр больше ${m} и число делится на ${n}? ${conditionE}`);

                rl.close();
              });
            });
          });
        });
      });
    });
  });
});