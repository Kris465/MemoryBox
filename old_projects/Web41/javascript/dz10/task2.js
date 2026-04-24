const prompt = require('prompt-sync')();

class ExtendedDate extends Date {
    constructor(year, month, day) {
        
        super(year, month, day);
    }

    
    toText() {
        const monthNames = [
            "января", "февраля", "марта", "апреля", "мая", "июня",
            "июля", "августа", "сентября", "октября", "ноября", "декабря"
        ];
        const day = this.getDate();
        const month = monthNames[this.getMonth()];
        return `${day} ${month}`;
    }

    
    isFutureOrCurrent() {
        const now = new Date();
        return this >= now; 
    }

  
    isLeapYear() {
        const year = this.getFullYear();
   
        return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
    }

   
    getNextDate() {
        return new ExtendedDate(this.getFullYear(), this.getMonth(), this.getDate() + 1);
    }
}


const year = parseInt(prompt("Введите год (например, 2023):"));
const month = parseInt(prompt("Введите месяц (1-12):")) - 1; 
const day = parseInt(prompt("Введите день (1-31):"));


const customDate = new ExtendedDate(year, month, day);


console.log("Дата текстом:", customDate.toText());
console.log("Это будущее или настоящее?:", customDate.isFutureOrCurrent());
console.log("Этот год високосный?:", customDate.isLeapYear());
console.log("Следующая дата:", customDate.getNextDate().toText());

