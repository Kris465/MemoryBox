const prompt = require('prompt-sync')();

function getDayType(k) {
    if (k < 1 || k > 365) {
        return "Некорректный ввод. k должно быть в диапазоне от 1 до 365.";
    }

    const dayOfWeek = (k - 1) % 7; 

    if (dayOfWeek === 5 || dayOfWeek === 6) {
        return `День ${k} года - выходной (суббота или воскресенье).`;
    } else {
        return `День ${k} года - рабочий день.`;
    }
}

const k = 15;
const result = getDayType(k);
console.log(result);