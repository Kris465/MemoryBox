const prompt = require('prompt-sync')();

function permutations(num) {
  const str = String(num);
  if (str.length !== 3 || new Set(str).size !== 3) return "Ошибка: некорректный ввод";
  const [a, b, c] = str;
  return [
    Number(a + b + c),
    Number(a + c + b),
    Number(b + a + c),
    Number(b + c + a),
    Number(c + a + b),
    Number(c + b + a),
  ];
}

const input = prompt("Введите трехзначное число с разными цифрами: ");
const result = permutations(Number(input));

if (typeof result === 'string') {
  console.log(result);
} else {
  console.log("Перестановки:", result);
}