
  
    function kishechnitrubochki(a, b) {
        if (a === 0) {
            return "Ошибка: a не может быть 0.";
        }
        return -b / a;
    }
    
    const prompt = require('prompt-sync')();
    
    const a = prompt("Введите a: ");
    const b = prompt("Введите b: ");
    
    const result = kishechnitrubochki(a, b);
    
    console.log(result);