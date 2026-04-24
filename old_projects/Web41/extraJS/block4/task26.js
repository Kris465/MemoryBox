function checkDigitsSum(number) {
    if (number < 10 || number > 99) {
        console.log("Пожалуйста, введите двузначное число.");
        return;
    }

    let firstDigit = Math.floor(number / 10);
    let secondDigit = number % 10; 

    let sumOfDigits = firstDigit + secondDigit;


    if (sumOfDigits % 3 === 0) {
        console.log(`Сумма цифр (${sumOfDigits}) кратна 3.`);
    } else {
        console.log(`Сумма цифр (${sumOfDigits}) не кратна 3.`);
    }

    if (number % sumOfDigits === 0) {
        console.log(`Сумма цифр (${sumOfDigits}) кратна числу ${number}.`);
    } else {
        console.log(`Сумма цифр (${sumOfDigits}) не кратна числу ${number}.`);
    }
}


let number = parseInt(prompt("Введите двузначное число:"));


if (!isNaN(number)) {
    checkDigitsSum(number);
} else {
    console.log("Пожалуйста, введите корректное число.");
}