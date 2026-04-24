const prompt = require('prompt-sync')();

function convertAgeInMonthsToYearsAndMonths(n) {
    if (n < 1 || n > 1188) {
        return "Введите натуральное число от 1 до 1188";
    }

    const years = Math.floor(n / 12);
    const months = n % 12;

    let result = '';

    if (years > 0) {
        result += years + (years === 1 ? ' год ' : ' года ');
    }

    if (months > 0) {
        result += months + (months === 1 ? ' месяц' : ' месяцев');
    } else if (years > 0) {
        result += 'ровно';
    }

    return result.trim();
}


console.log(convertAgeInMonthsToYearsAndMonths(21));  
console.log(convertAgeInMonthsToYearsAndMonths(52));   
console.log(convertAgeInMonthsToYearsAndMonths(46));   
console.log(convertAgeInMonthsToYearsAndMonths(12));   
console.log(convertAgeInMonthsToYearsAndMonths(0));    