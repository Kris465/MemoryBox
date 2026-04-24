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

  const digits = numStr.split('').map(Number);
  const firstDigit = digits[0];
  const lastDigit = digits[digits.length -1];


  const sumDigits = digits.reduce((sum, d) => sum + d, 0);
  
  const prodDigits = digits.reduce((prod, d) => prod * d, 1);

  const countDigits = digits.length;


  const conditionA = sumDigits >10;
  

  const conditionB = prodDigits <50;

  
  const conditionC = countDigits %2 ===0;

 
  const numValue = Number(numStr);
  const conditionD = numValue >=1000 && numValue <=9999;

  
  const conditionE = firstDigit <=6;


  const conditionF = firstDigit === lastDigit;

  const comparisonFirstLast = firstDigit > lastDigit ? 'первая' : (firstDigit < lastDigit ? 'последняя' : 'они равны');

  
  console.log(`а) Сумма цифр больше 10? ${conditionA}`);
  console.log(`б) Произведение цифр меньше 50? ${conditionB}`);
  console.log(`в) Количество цифр чётное? ${conditionC}`);
  
  
  console.log(`г) Число четырёхзначное? ${conditionD}`);
  
  console.log(`д) Первая цифра не превышает6? ${conditionE}`);
  
  console.log(`е) Начинается и заканчивается одной и той же цифрой? ${conditionF}`);
  
  console.log(`ж) Какая из его цифр больше: первая или последняя? ${comparisonFirstLast}`);

  
rl.close();
});