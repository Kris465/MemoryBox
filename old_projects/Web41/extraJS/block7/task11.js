console.log("б) Трехзначные числа, кратные 7 и сумма их цифр кратна 7:");

for (let num = 100; num <= 999; num++) {
    if (num % 7 === 0) {
        const hundreds = Math.floor(num / 100);
        const tens = Math.floor((num % 100) / 10);
        const units = num % 10;
        const sumDigits = hundreds + tens + units;

        if (sumDigits % 7 === 0) {
            console.log(num);
        }
    }
}