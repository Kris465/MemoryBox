const prompt = require('prompt-sync')();

function calculator() {
    // Запрашиваем у пользователя ввод математического выражения
    const expression = prompt("Введите математическое выражение (например, 5 + 10):");

   
    try {
        
        const sanitizedExpression = expression.replace(/\s+/g, '');

      
        if (/^[\d+\-*/.]+$/.test(sanitizedExpression)) {
            
            const result = eval(sanitizedExpression);
            console.log(`Результат: ${result}`);
        } else {
            console.log('Ошибка: Введите корректное математическое выражение.');
        }
    } catch (error) {
        console.log('Ошибка при вычислении: ' + error.message);
    }
}


calculator();