const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

console.log('Введите последовательность вещественных чисел, завершающуюся числом 1000. Вводите числа через пробел.');

rl.question('> ', (input) => {
  const arr = input.trim().split(/\s+/).map(Number);
  if (arr.length === 0 || arr[arr.length -1] !== 1000) {
    console.log('Последовательность должна заканчиваться числом 1000.');
    rl.close();
    return;
  }

  let countEqualSeq = 1;
  let totalEqualSequences = 0;
  let distinctCount = 0;
  
  let prev = null;
  
  for (let i=0; i<arr.length; i++) {
    const current = arr[i];
    if (i ===0) {
      prev = current;
      distinctCount++;
    } else {
      if (current === prev) {
        countEqualSeq++;
      } else {
        if (countEqualSeq >1) {
          totalEqualSequences++;
        }
        countEqualSeq=1;
        distinctCount++;
      }
      prev = current;
    }
    if (current ===1000) break;
  }

  if (arr.length >1 && arr[arr.length -2] === arr[arr.length -1]) {
    totalEqualSequences++;
  }

  console.log(`Количество серий равных чисел: ${totalEqualSequences}`);
  console.log(`Количество различных чисел: ${distinctCount}`);

  rl.close();
});