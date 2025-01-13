function combineDigits(digit1, digit2, digit3) {
    // Преобразуем цифры в строку и объединяем их
    const combinedString = String(digit1) + String(digit2) + String(digit3);
    // Преобразуем строку обратно в число
    const combinedNumber = Number(combinedString);
    return combinedNumber;
}

const digit1 = 1;
const digit2 = 4;
const digit3 = 9;

const result = combineDigits(digit1, digit2, digit3);
console.log(`Объединенные цифры: ${result}`);
