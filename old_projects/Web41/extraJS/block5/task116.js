const prompt = require('prompt-sync')();

function isPalindrome(str) {
    str = str.replace(/\s+/g, '').toLowerCase();
    return str === str.split('').reverse().join('');
}

let phrases = [
    "АРГЕНТИНА МАНИТ НЕГРА",
    "ПОТ КАК ПОТОП",
    "А РОЗА УПАЛА НА ЛАПУ АЗОРА"
];

phrases.forEach(phrase => {
    let result = isPalindrome(phrase);
    console.log(`"${phrase}" является перевертышем: ${result}`);
});