const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let x;
let a = [];
let n;

function askQuestion(query) {
  return new Promise(resolve => rl.question(query, resolve));
}

async function main() {
  x = parseInt(await askQuestion('Введите натуральное число x: '), 10);
  
  for (let i = 0; i < x; i++) {
    const numStr = await askQuestion(`Введите число a${i + 1}: `);
    a.push(parseInt(numStr, 10));
  }
  
  n = parseInt(await askQuestion('Введите число n: '), 10);
  
  let sum = 0;
  let count = 0;
  
  for (let num of a) {
    if (num > n) {
      sum += num;
      count++;
    }
  }
  
  const average = sum / count;
  
  console.log(`Среднее арифметическое чисел больше ${n}: ${average}`);
  
  rl.close();
}

main();