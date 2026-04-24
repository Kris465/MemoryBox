const numberStr = prompt("Введите натуральное число:");
const num = parseInt(numberStr, 10);
let divisor = 2;
while (divisor <= num) {
    if (num % divisor === 0) {
        console.log(`Наименьший делитель, отличный от 1: ${divisor}`);
        break;
    }
    divisor++;
}