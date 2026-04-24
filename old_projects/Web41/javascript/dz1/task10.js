const prompt = require('prompt-sync')();
let userNumber = prompt();
if (userNumber % 2 == 0 ) {
    console.log('число чётное')
} else {
    console.log('число не чётное')
}