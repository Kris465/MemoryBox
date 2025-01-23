const prompt = require('prompt-sync')();

   let x = prompt('Введите число для проверки: ');
   let st = Math.floor(Math.log2(x)); 
    function power(x) {
        if (Math.log2(x) % 1 === 0) {
            console.log(`Число ${x} является ${st} степенью двойки.`);
        } else {
            console.log(`Число ${x} не является степенью двойки.`);
        }
    }

power(x);



