const prompt = require('prompt-sync')();

     function getSeason(monthNumber) {
         if (monthNumber < 1 || monthNumber > 12) {
             return "Некорректный номер месяца. Пожалуйста, введите число от 1 до 12.";
         }

         if (monthNumber >= 3 && monthNumber <= 5) {
             return "Весна";
         } else if (monthNumber >= 6 && monthNumber <= 8) {
             return "Лето";
         } else if (monthNumber >= 9 && monthNumber <= 11) {
             return "Осень";
         } else {
             return "Зима";
         }
     }

     const monthNumber = parseInt(prompt("Введите номер месяца (1-12):"), 10);
     const season = getSeason(monthNumber);

     console.log(season);
    