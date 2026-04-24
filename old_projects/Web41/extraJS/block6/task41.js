const prompt = require('prompt-sync')();

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Введите натуральное число: ', (input) => {
  const n = input.trim();

  if (!/^\d+$/.test(n)) {
    console.log('Пожалуйста, введите натуральное число.');
    rl.close();
    return;
  }

  const digits = n.split('').map(Number);
  const maxDigits = [...digits].sort((a, b) => b - a).slice(0, 2);
  const minDigits = [...digits].sort((a, b) => a - b).slice(0, 2);

  console.log(`Две максимальные цифры: ${maxDigits.join(', ')}`);
  console.log(`Две минимальные цифры: ${minDigits.join(', ')}`);

  rl.close();
});