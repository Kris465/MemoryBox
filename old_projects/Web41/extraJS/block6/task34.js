const result = [];
let num = 100;
while (result.length < 15) {
  if (num % 19 === 0) {
    result.push(num);
  }
  num++;
}
console.log(result);