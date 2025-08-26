const prompt = require('prompt-sync')();

const classSizes = [];

for (let i = 0; i < 20; i++) {
    let input;
    do {
        input = prompt(`Введите число учеников в классе ${i + 1}:`);
        if (input === null) continue;
        input = input.trim();
    } while (input === '' || !/^\d+$/.test(input));
    classSizes.push(parseInt(input, 10));
}

const maxSize = Math.max(...classSizes);
const minSize = Math.min(...classSizes);
const difference = maxSize - minSize;

console.log(`Разница между размером самого большого и самого маленького класса: ${difference}`);