const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите натуральное число (n > 999): "));

if (n <= 999) {
    console.log("Ошибка: число должно быть больше 999.");
} else {
    
    const hundreds = Math.floor((n % 1000) / 100);

   
    const thousands = Math.floor(n / 1000) % 10;

    
    console.log(`Число сотен: ${hundreds}`);
    console.log(`Число тысяч: ${thousands}`);
}