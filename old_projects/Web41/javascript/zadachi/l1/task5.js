const prompt = require('prompt-sync')();
let x = prompt('введите число от 0 до 10: ');
if (x % 2 ==0) {
    console.log('истина')
} else {
    console.log('ложь')
}