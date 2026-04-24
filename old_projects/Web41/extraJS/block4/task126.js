const prompt = require('prompt-sync')();
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function getMushroomWord(k) {
    const lastDigit = k % 10;
    const lastTwoDigits = k % 100;

    if (lastDigit === 1 && lastTwoDigits !== 11) {
        return "гриб";
    } else if ((lastDigit >= 2 && lastDigit <= 4) && (lastTwoDigits < 12 || lastTwoDigits > 14)) {
        return "гриба";
    } else {
        return "грибов";
    }
}

rl.question("Введите натуральное число k: ", (input) => {
    const k = parseInt(input, 10);

    if (k > 0) {
        const mushroomWord = getMushroomWord(k);
        console.log(`Мы нашли ${k} ${mushroomWord} в лесу.`);
    } else {
        console.log("Пожалуйста, введите натуральное число больше 0.");
    }

    rl.close(); 
});
