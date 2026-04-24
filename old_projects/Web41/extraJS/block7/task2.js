const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline.question('Введите число a: ', (a) => {
  readline.question('Введите число b: ', (b) => {
    readline.question('Введите число c: ', (c) => {
      a = parseInt(a);
      b = parseInt(b);
      c = parseInt(c);

      if (isNaN(a) || isNaN(b) || isNaN(c)) {
        console.log("Пожалуйста, введите целые числа.");
        readline.close();
        return;
      }

      if (a > b) {
        console.log("Число a должно быть меньше или равно числу b.");
        readline.close();
        return;
      }

      console.log(`Числа от ${a} до ${b}, кратные ${c}:`);
      for (let i = a; i <= b; i++) {
        if (i % c === 0) {
          console.log(i);
        }
      }

      readline.close();
    });
  });
});
