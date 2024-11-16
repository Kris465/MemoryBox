process.stdin.setEncoding('utf8');
const prompt = require('prompt-sync')();

function isPalindrome(str) {
    const cleanedStr = str.replace(/[^а-яА-ЯёЁa-zA-Z0-9]/g, '').toLowerCase();
    const reversedStr = cleanedStr.split('').reverse().join('');
    return cleanedStr === reversedStr;
}

// Получаем ввод от пользователя
const userInput = prompt('Введите строку для проверки на палиндром: ');

// Проверяем и выводим результат
if (isPalindrome(userInput)) {
    console.log('Это палиндром!');
} else {
    console.log('Это не палиндром.');
}
