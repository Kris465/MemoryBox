
function sumOfIntegers(start, end) {
    let sum = 0;
    for (let i = start; i <= end; i++) {
        sum += i;
    }
    return sum;
}

let sumA = sumOfIntegers(100, 500);
console.log("Сумма всех целых чисел от 100 до 500:", sumA);

let a = parseInt(prompt("Введите значение a (a < 500):"));
if (a < 500) {
    let sumB = sumOfIntegers(a, 500);
    console.log(`Сумма всех целых чисел от ${a} до 500:`, sumB);
} else {
    console.log("Ошибка: a должно быть меньше 500.");
}

let b = parseInt(prompt("Введите значение b (b > -10):"));
if (b > -10) {
    let sumC = sumOfIntegers(-10, b);
    console.log(`Сумма всех целых чисел от -10 до ${b}:`, sumC);
} else {
    console.log("Ошибка: b должно быть больше -10.");
}

let aInput = parseInt(prompt("Введите значение a:"));
let bInput = parseInt(prompt("Введите значение b (b > a):"));
if (bInput > aInput) {
    let sumD = sumOfIntegers(aInput, bInput);
    console.log(`Сумма всех целых чисел от ${aInput} до ${bInput}:`, sumD);
} else {
    console.log("Ошибка: b должно быть больше a.");
}