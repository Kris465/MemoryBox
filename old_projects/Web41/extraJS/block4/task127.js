const prompt = require('prompt-sync')();

function formatPrice(n) {
    const rubles = Math.floor(n / 100); 
    const kopecks = n % 100; 

    let rubleWord;
    let kopeckWord;


    if (rubles === 1) {
        rubleWord = "рубль";
    } else if (rubles >= 2 && rubles <= 4) {
        rubleWord = "рубля";
    } else {
        rubleWord = "рублей";
    }


    if (kopecks === 1) {
        kopeckWord = "копейка";
    } else if (kopecks >= 2 && kopecks <= 4) {
        kopeckWord = "копейки";
    } else {
        kopeckWord = "копеек";
    }

   
    if (rubles === 0 && kopecks === 0) {
        return "Стоимость равна нулю.";
    } else if (rubles === 0) {
        return `${kopecks} ${kopeckWord} ровно`;
    } else if (kopecks === 0) {
        return `${rubles} ${rubleWord} ровно`;
    } else {
        return `${rubles} ${rubleWord} ${kopecks} ${kopeckWord}`;
    }
}


const n = parseInt(prompt("Введите стоимость товара в копейках (от 1 до 9999):"), 10);

if (n >= 1 && n <= 9999) {
    console.log(formatPrice(n));
} else {
    console.log("Пожалуйста,  ВВЕДИЕвведите натуральное число от 1 до 9999.");
}