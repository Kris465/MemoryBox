const prompt = require('prompt-sync')();

function calculateAge(birthYear, birthMonth, currentYear, currentMonth) {
    let age = currentYear - birthYear;


    if (currentMonth < birthMonth) {
        age--;
    }

  
    return age;
}


const birthYear = parseInt(prompt("Введите год рождения (например, 1990):"));
const birthMonth = parseInt(prompt("Введите номер месяца рождения (1-12):"));
const currentYear = parseInt(prompt("Введите текущий год (например, 2023):"));
const currentMonth = parseInt(prompt("Введите текущий номер месяца (1-12):"));


if (birthMonth < 1 || birthMonth > 12 || currentMonth < 1 || currentMonth > 12) {
    console.log("Номер месяца должен быть в диапазоне от 1 до 12.");
} else {

    const age = calculateAge(birthYear, birthMonth, currentYear, currentMonth);
    console.log(`Возраст человека: ${age} полных лет.`);
}