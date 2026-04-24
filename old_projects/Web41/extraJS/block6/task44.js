const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

console.log('Введите последовательность вещественных чисел, завершающуюся нулём. Вводите числа через пробел.');

rl.question('> ', (input) => {
  const arr = input.trim().split(/\s+/).map(Number);
  if (arr.length === 0 || arr[arr.length -1] !== 0) {
    console.log('Последовательность должна заканчиваться числом 0.');
    rl.close();
    return;
  }

  let countDistinct = 0;
  let prev = null;

  for (let i=0; i<arr.length; i++) {
    const current = arr[i];
    if (current === 0) break; 
    if (i===0 || current !== prev) {
      countDistinct++;
    }
    prev = current;
  }

  console.log(`Количество различных чисел: ${countDistinct}`);

  rl.close();
});