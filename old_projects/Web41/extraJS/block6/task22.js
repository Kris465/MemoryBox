let count3 = 0;
let lastDigit = digits[digits.length - 1];
let countLastDigit = 0;
let countEven = 0;
let sumGreaterFive = 0;
let productGreaterSeven = 1;
let countZeroAndFive = 0;

for (let d of digits) {
    if (d === '3') {
        count3++;
    }
    if (d === lastDigit) {
        countLastDigit++;
    }
    if (parseInt(d) % 2 === 0) {
        countEven++;
    }
    if (parseInt(d) > 5) {
        sumGreaterFive += parseInt(d);
    }
    if (parseInt(d) > 7) {
        productGreaterSeven *= parseInt(d);
    }
    if (d === '0' || d === '5') {
        countZeroAndFive++;
    }
}

console.log("а) Количество цифр 3: " + count3);
console.log("б) Сколько раз встречается последняя цифра: " + countLastDigit);
console.log("в) Количество четных цифр: " + countEven);
console.log("г) Сумма цифр, больших пяти: " + sumGreaterFive);
console.log("д) Произведение цифр, больших семи: " + productGreaterSeven);
console.log("е) Количество цифр 0 и 5: " + countZeroAndFive);