const prompt = require('prompt-sync')();

let numbers = [];
while (numbers.length < 10) {
    let randomNum = Math.floor(Math.random() * 20) + 1;
    if (randomNum % 4 !== 0 && !numbers.includes(randomNum)) {
        numbers.push(randomNum);
    }
}

console.log(numbers.join(' '));
