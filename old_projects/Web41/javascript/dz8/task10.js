const prompt = require('prompt-sync')();

function formatString(template, ...args) {
    return template.replace(/%(\d+)/g, (match, index) => {
        const argIndex = parseInt(index, 10);
        return argIndex < args.length ? args[argIndex] : match;
    });
}

const template = prompt("Enter a string template (e.g., 'Hello, %0! Today is %1.'): ");
const parameters = prompt("Enter parameters separated by commas (e.g., 'Alex, nice weather'): ");
const args = parameters.split(',').map(param => param.trim());


const result = formatString(template, ...args);
console.log(result);