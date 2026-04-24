
const prompt = require('prompt-sync')(); 

function gcd(a, b) {
    while (b !== 0) {
        const temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Введите три натуральных числа через пробел: ', (input) => {
    const nums = input.trim().split(/\s+/).map(Number);
    if (nums.length !== 3 || nums.some(n => !Number.isInteger(n) || n <= 0)) {
        console.log('Пожалуйста, введите три натуральных числа.');
        rl.close();
        return;
    }

    const [a, b, c] = nums;

    const gcdAB = gcd(a, b);
   
    const gcdABC = gcd(gcdAB, c);

    console.log(`Наибольший общий делитель трех чисел: ${gcdABC}`);

    rl.close();
});