function countFirstDigitOccurrences(number) {
  const numStr = number.toString();
  
  const firstDigit = numStr[0];

  let count = 0;
  for (let digit of numStr) {
    if (digit === firstDigit) {
      count++;
    }
  }
  
  return count;
}

const number = 1234512345;
console.log(`В числе ${number} первая цифра встречается ${countFirstDigitOccurrences(number)} раз.`);