function productOfIntegers(start, end) {
    let product = 1;
    for (let i = start; i <= end; i++) {
        product *= i;
    }
    return product;
}

let productA = productOfIntegers(8, 15);
console.log("Произведение всех целых чисел от 8 до 15:", productA);

let a = parseInt(prompt("Введите значение a (1 <= a <= 20):"));
if (a >= 1 && a <= 20) {
    let productB = productOfIntegers(a, 20);
    console.log(`Произведение всех целых чисел от ${a} до 20:`, productB);
} else {
    console.log("Ошибка: a должно быть в диапазоне от 1 до 20.");
}

let b = parseInt(prompt("Введите значение b (1 <= b <= 20):"));
if (b >= 1 && b <= 20) {
    let productC = productOfIntegers(1, b);
    console.log(`Произведение всех целых чисел от 1 до ${b}:`, productC);
} else {
    console.log("Ошибка: b должно быть в диапазоне от 1 до 20.");
}

let aInput = parseInt(prompt("Введите значение a:"));
let bInput = parseInt(prompt("Введите значение b (b > a):"));
if (bInput > aInput) {
    let productD = productOfIntegers(aInput, bInput);
    console.log(`Произведение всех целых чисел от ${aInput} до ${bInput}:`, productD);
} else {
    console.log("Ошибка: b должно быть больше a.");
}