const prompt = require('prompt-sync')();

function calculateAge() {

    const birthYear = parseInt(prompt("Введите год рождения:"));
    const birthMonth = parseInt(prompt("Введите месяц рождения (1-12):"));
    const birthDay = parseInt(prompt("Введите день рождения:"));
    
    const currentYear = parseInt(prompt("Введите текущий год:"));
    const currentMonth = parseInt(prompt("Введите текущий месяц (1-12):"));
    const currentDay = parseInt(prompt("Введите текущий день:"));
    
    let age = currentYear - birthYear;
    
    if (currentMonth < birthMonth || (currentMonth === birthMonth && currentDay < birthDay)) {
        age--; 
    }
    
    console.log(`Возраст: ${age} полных лет`);
}

calculateAge();