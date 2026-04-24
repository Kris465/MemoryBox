const prompt = require('prompt-sync')();

function getDayType(dayOfWeek) {
    if (dayOfWeek === 6) return "суббота";
    if (dayOfWeek === 7) return "воскресенье";
    return "рабочий день";
}

function taskA(k) {
    let dayOfWeek = ((k - 1) % 7) + 1;
    return getDayType(dayOfWeek);
}

function taskB(k, d) {
    let dayOfWeek = ((d - 1) + (k - 1)) % 7 + 1;
    return getDayType(dayOfWeek);
}

let k = parseInt(prompt("Введите номер дня года k (от 1 до 365):"),10);
if (!(k >=1 && k <=365)) {
    console.log("Ошибка: k должно быть от 1 до 365");
} else {
    let resultA = taskA(k);
    console.log(`(а) При условии, что 1 января — понедельник, ${k}-й день года будет: ${resultA}`);
    
    let d = parseInt(prompt("Введите номер дня недели для 1 января d (понедельник=1,...,воскресенье=7):"),10);
    
    if (!(d >=1 && d <=7)) {
        console.log("Ошибка: d должно быть от 1 до 7");
    } else {
        let resultB = taskB(k,d);
        console.log(`(б) При условии, что ${d}-й день недели — это день недели для 1 января, ${k}-й день года будет: ${resultB}`);
    }
}