

function getDaysInMonth(month, year) {

    const daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    return daysInMonth[month - 1]; 
}

function getPreviousDate(m, n) {
    if (m < 1 || m > 12 || n < 1 || n > getDaysInMonth(m)) {
        return "Некорректная дата.";
    }

    if (n > 1) {
        return `${m}-${n - 1}`;
    } else {
        
        if (m === 1) {
            return `12-${31}`;
        } else {
            const previousMonth = m - 1;
            const previousDay = getDaysInMonth(previousMonth);
            return `${previousMonth}-${previousDay}`;
        }
    }
}

function getNextDate(m, n) {
    if (m < 1 || m > 12 || n < 1 || n > getDaysInMonth(m)) {
        return "Некорректная дата.";
    }

    if (n < getDaysInMonth(m)) {
        return `${m}-${n + 1}`;
    } else {

        if (m === 12) {
            return `1-${1}`;
        } else {
            const nextMonth = m + 1;
            return `${nextMonth}-1`;
        }
    }
}

const m = parseInt(prompt("Введите номер месяца (1-12):"), 10);
const n = parseInt(prompt("Введите число (день):"), 10);

const previousDate = getPreviousDate(m, n);
const nextDate = getNextDate(m, n);

console.log(`Предыдущая дата: ${previousDate}`);
console.log(`Следующая дата: ${nextDate}`);