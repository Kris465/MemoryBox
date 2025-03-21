const prompt = require('prompt-sync')();

function combineStrings(...strings) {
    return strings.join(' ');
}

function main() {
    const inputStrings = [];
    let input;

    console.log("Введите строки для объединения (введите 'exit' для завершения):");

    while (true) {
        input = prompt('> ');
        if (input.toLowerCase() === 'exit') {
            break;
        }
        inputStrings.push(input);
    }

    const result = combineStrings(...inputStrings);
    console.log("Объединенная строка:");
    console.log(result);
}

main();
