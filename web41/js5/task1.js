const readline = require('readline');


const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function stringFrom(...args) {
    return args.join(' ');
}


function collectStrings() {
    const strings = [];

    function askForInput() {
        rl.question('Введите строку (или "стоп" для завершения): ', (input) => {
            if (input.toLowerCase() === 'стоп') {
                
                console.log(stringFrom(...strings));
                rl.close();
            } else {
                strings.push(input);
                askForInput();
            }
        });
    }

    askForInput();
}

collectStrings();
