const prompt = require("prompt-sync")();

function isPalindrome(str) {
    const cleanedStr = str.replace(/[^а-яА-ЯёЁA-Za-z0-9]/g, '').toLowerCase();
    const reversedStr = cleanedStr.split('').reverse().join('');
    return cleanedStr === reversedStr;
}

const userIput = prompt("Введите строку: ");

if (isPalindrome(userIput)) {
    console.log("Это палиндром");
} else {
    console.log("Это не палиндром");
}
