const prompt = require('prompt-sync')();

function getMonth(n) {
    return (n % 12) + 1;
  }
  

  const n = Number(prompt("Введите значение : "))
  const x = getMonth(n);
  console.log(x);
  console.log(`При n = ${n}, x = ${x}`); 