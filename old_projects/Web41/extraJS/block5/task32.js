function calculateSum(n) {
    let sumOfOnes = n; 
    let sumOfNumbers = (n * (n + 1)) / 2; 
    return sumOfOnes + sumOfNumbers;
}

let n = parseInt(prompt("Введите натуральное число n:"));
if (n > 0) {
    let result = calculateSum(n);
    console.log(`Сумма последовательности от 1 до ${n} с ${n} единицами:`, result);
} else {
    console.log("Ошибка: n должно быть натуральным числом.");
}