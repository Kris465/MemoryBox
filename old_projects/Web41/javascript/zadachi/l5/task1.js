const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function stringFrom(...args) {
    return args.join(" ");
}

function colectStrings(){
    const strings = [];

    function askForInput(){
        rl.question("Введите строку или стоп: ", (input) => {
            if (input.toLowCase() == "stop") {
                console.log(stringFrom(...strings));
            } else {
                strings.push(input);
                askForInput();
            }
        });
    }
    askForInput();
}

colectStrings();