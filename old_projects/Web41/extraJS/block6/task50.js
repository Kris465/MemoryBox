const prompt = require('prompt-sync')(); 

const numberInput = prompt("Введите натуральное число:");
const a = prompt("Введите цифру a:");
const b = prompt("Введите цифру b:");
const k = parseInt(prompt("Введите число k:"), 10);
const number = parseInt(numberInput, 10);

if (isNaN(number) || number <= 0 || a.length !== 1 || b.length !== 1 || isNaN(k)) {
    console.log("Некорректный ввод");
} else {
    const numberStr = number.toString();
    const hasA = numberStr.includes(a);
    const noB = !numberStr.includes(b);
    const countA = [...numberStr].filter(d => d === a).length;
    const aMoreKTimes = countA > k;
    const hasAandB = numberStr.includes(a) && numberStr.includes(b);

    console.log(`а) Есть ли в числе цифра ${a}? ${hasA ? 'Да' : 'Нет'}`);
    console.log(`б) Верно ли, что в числе нет цифры ${b}? ${noB ? 'Да' : 'Нет'}`);
    console.log(`в) Верно ли, что цифра ${a} встречается более ${k} раз? ${aMoreKTimes ? 'Да' : 'Нет'}`);
    console.log(`г) Есть ли в числе цифры ${a} и ${b}? ${hasAandB ? 'Да' : 'Нет'}`);
}