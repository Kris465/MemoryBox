function analyzeFourDigitNumber(number, a) {
    if (number < 1000 || number > 9999) {
        console.log("Пожалуйста, введите четырехзначное число.");
        return;
    }

    const numStr = number.toString();
    
    const firstDigit = parseInt(numStr[0]);
    const secondDigit = parseInt(numStr[1]);
    const thirdDigit = parseInt(numStr[2]);
    const fourthDigit = parseInt(numStr[3]);

    const sumFirstTwo = firstDigit + secondDigit;
    const sumLastTwo = thirdDigit + fourthDigit;
    const isSumEqual = sumFirstTwo === sumLastTwo;
    console.log(`Сумма двух первых цифр равна сумме двух последних: ${isSumEqual}`);

    const totalSum = firstDigit + secondDigit + thirdDigit + fourthDigit;
    const isSumDivisibleByThree = totalSum % 3 === 0;
    console.log(`Сумма всех цифр кратна трем: ${isSumDivisibleByThree}`);


    const product = firstDigit * secondDigit * thirdDigit * fourthDigit;
    const isProductDivisibleByFour = product % 4 === 0;
    console.log(`Произведение всех цифр кратно четырем: ${isProductDivisibleByFour}`);


    const isProductDivisibleByA = a !== 0 && product % a === 0; 
    console.log(`Произведение всех цифр кратно числу ${a}: ${isProductDivisibleByA}`);
}

let number = parseInt(prompt("Введите четырехзначное число:"));
let a = parseInt(prompt("Введите число a:"));
if (!isNaN(number) && !isNaN(a)) {
    analyzeFourDigitNumber(number, a);
} else {
    console.log("Пожалуйста, введите корректные числа.");
}