const prompt = require('prompt-sync')();

function toCamelCase(cssString) {
return cssString
    .split('-') 
    .map((word, index) => {
            if (index === 0) {
                return word; 
            }
            return word.charAt(0).toUpperCase() + word.slice(1);
        })
        .join(''); 
}

const style = prompt("введите css стиль: ");

console.log(toCamelCase(`${style}`));