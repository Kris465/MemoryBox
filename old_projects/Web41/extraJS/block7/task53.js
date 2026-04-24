const n = parseInt(prompt("Введите n:"));
const inputStr = prompt(`Введите ${n} целых чисел через пробел:`);
const a = inputStr.trim().split(' ').map(Number);


if (a.length !== n) {
  alert("Количество введённых чисел не совпадает с n");
} else {
  let maxValue = a[0];
  let minValue = a[0];
  let maxIndex = 0; 
  let minIndex = 0; 

  for (let i = 0; i < n; i++) {
    if (a[i] >= maxValue) {
      maxValue = a[i];
      maxIndex = i; 
    }
    if (a[i] < minValue) {
      minValue = a[i];
      minIndex = i; 
    }
  }

  console.log(maxIndex + 1);
  console.log(minIndex + 1);
}