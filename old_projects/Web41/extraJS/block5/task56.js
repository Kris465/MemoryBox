
let n = 5;
let a = [1, 2, 3, 4, 5];

let sum_a = 0;
for (let i = 0; i < n; i++) {
    sum_a += a[i];
}


let product_a = 1;
for (let i = 0; i < n; i++) {
    product_a *= a[i];
}


let sum_squares = 0;
for (let i = 0; i < n; i++) {
    sum_squares += a[i] * a[i];
}


let sum_reciprocals = 0;
for (let i = 0; i < n; i++) {
    sum_reciprocals += 1 / a[i];
}


console.log("Сумма:", sum_a);
console.log("Произведение:", product_a);
console.log("Сумма квадратов:", sum_squares);
console.log("Сумма дробей:", sum_reciprocals);