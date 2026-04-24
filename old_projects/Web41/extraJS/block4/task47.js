const prompt = require('prompt-sync')();

function checkDigits(number) {

    if (number < 10 || number > 99) {
        return "Ошибка: число должно быть двузначным.";
    }

    const tens = Math.floor(number / 10);
    const units = number % 10; 

    const hasFourOrSeven = (tens === 4 || tens === 7 || units === 4 || units === 7);
    
    const hasThreeSixOrNine = (tens === 3 || tens === 6 || tens === 9 || units === 3 || units === 6 || units === 9);

    return {
        hasFourOrSeven: hasFourOrSeven,
        hasThreeSixOrNine: hasThreeSixOrNine
    };
}

try {
    let number = parseInt(prompt("Введите двузначное число:"), 10);

    if (!isNaN(number) && number >= 10 && number <= 99) {
        const result = checkDigits(number);
        
        console.log(`Цифры 4 или 7 входят в число: ${result.hasFourOrSeven ? "Да" : "Нет"}`);
        console.log(`Цифры 3, 6 или 9 входят в число: ${result.hasThreeSixOrNine ? "Да" : "Нет"}`);
    } else {
        throw new Error("Пожалуйста, введите корректное двузначное число.");
    }
} catch (error) {
    console.error("Произошла ошибка:", error.message);
}