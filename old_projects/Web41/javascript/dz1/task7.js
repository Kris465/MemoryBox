const prompt = require('prompt-sync')();
let skolko = prompt('введите количество файлов: ');
const razmer = 820
let result = skolko * 1024 / razmer
console.log(`в ${skolko} gb поместится ${result} файлов `)