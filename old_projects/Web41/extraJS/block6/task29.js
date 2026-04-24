function findDigitPositions(numberStr) {
  const digits = numberStr.split('').map(Number);
  const n = digits.length;

  const maxDigit = Math.max(...digits);
  const minDigit = Math.min(...digits);

  const maxPosStart = digits.indexOf(maxDigit) + 1;
  const minPosStart = digits.indexOf(minDigit) + 1;

  const maxPosEnd = n - maxPosStart + 1;
  const minPosEnd = n - minPosStart + 1;

  return {
    maxFromStart: maxPosStart,
    minFromStart: minPosStart,
    maxFromEnd: maxPosEnd,
    minFromEnd: minPosEnd
  };
}

const numberInput = "391764"; 
const positions = findDigitPositions(numberInput);
console.log(positions);