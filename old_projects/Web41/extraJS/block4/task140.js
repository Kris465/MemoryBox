const prompt = require('prompt-sync')();
function digitCount(num) {
    let count = 0;
    while (num > 0) {
      num = Math.floor(num / 10);
      count++;
    }
    return count;
  }
  
  function getDigit(num, pos) {
   
    const len = digitCount(num);
    let divisor = Math.pow(10, len - pos);
    return Math.floor(num / divisor) % 10;
  }
  
  function findKthDigit(k) {
    for (let num = 1; num <= 110; num++) {
      let len = digitCount(num);
      if (k <= len) {
        return getDigit(num, k);
      } else {
        k -= len;
      }
    }
    return -1; 
  }
  
  
  const k = parseInt(prompt("Введите k (1 ≤ k ≤ 222):"),10);
  
  if (k <1 || k >222) {
    console.log("k вне диапазона");
  } else {
    const digit = findKthDigit(k);
    console.log(digit);
  }