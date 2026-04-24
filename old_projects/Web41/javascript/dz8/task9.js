const prompt = require('prompt-sync')();

function customSplit(str, delimiter) {
    const result = [];
    let currentSubstring = '';

    for (let i = 0; i < str.length; i++) {
        const char = str[i];

        if (char === delimiter) {
            result.push(currentSubstring);
            currentSubstring = ''; 
        } else {
            currentSubstring += char; 
        }
    }


    if (currentSubstring) {
        result.push(currentSubstring);
    }

    return result;
}


const inputString = prompt("Введите строку для разбиения:");
const delimiter = prompt("Введите разделитель:");
const result = customSplit(inputString, delimiter);


console.log(result);