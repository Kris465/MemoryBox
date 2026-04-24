const prompt = require('prompt-sync')();

function compareAges() {

    const year1 = parseInt(prompt("Введите год рождения первого человека:"));
    const month1 = parseInt(prompt("Введите месяц рождения первого человека (1-12):"));
    const day1 = parseInt(prompt("Введите день рождения первого человека:"));
    

    const year2 = parseInt(prompt("Введите год рождения второго человека:"));
    const month2 = parseInt(prompt("Введите месяц рождения второго человека (1-12):"));
    const day2 = parseInt(prompt("Введите день рождения второго человека:"));
    

    if (year1 < year2) {
        console.log("Первый человек старше");
    } else if (year1 > year2) {
        console.log("Второй человек старше");
    } else {

        if (month1 < month2) {
            console.log("Первый человек старше");
        } else if (month1 > month2) {
            console.log("Второй человек старше");
        } else {
           
            if (day1 < day2) {
                console.log("Первый человек старше");
            } else if (day1 > day2) {
                console.log("Второй человек старше");
            } else {
                console.log("Оба человека родились в один день!");
            }
        }
    }
}


compareAges();