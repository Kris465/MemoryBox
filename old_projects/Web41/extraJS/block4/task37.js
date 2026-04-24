const prompt = require('prompt-sync')();        

function isInInterval(number) {
    return number > -5 && number < 3;
}


try {
    let input = prompt("Введите число:");
    let number = parseFloat(input); 

    if (!isNaN(number) && isFinite(number)) {
        if (isInInterval(number)) {
            console.log(`Число ${number} принадлежит интервалу (-5, 3).`);
        } else {
            console.log(`Число ${number} не принадлежит интервалу (-5, 3).`);
        }
    } else {
        throw new Error("Пожалуйста, введите корректное число.");
    }
} catch (error) {
    console.error("Произошла ошибка:", error.message);
}