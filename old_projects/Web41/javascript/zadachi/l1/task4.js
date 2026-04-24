const prompt = require('prompt-sync')();
let x = prompt('введите число: ')
if (x >=0 && x<=9) {
    console.log('истина')
} else {
    console.log('ложь')
}
