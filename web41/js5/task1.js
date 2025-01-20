const readline = require('readline');

// Создаем интерфейс для ввода/вывода
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function stringFrom(...args) {
    return args.join(' ');
}

// Функция для сбора строк от пользователя
function collectStrings() {
    const strings = [];

    function askForInput() {
        rl.question('Введите строку (или "стоп" для завершения): ', (input) => {
            if (input.toLowerCase() === 'стоп') {
                // Когда пользователь вводит "стоп", вызываем stringFrom
                console.log(stringFrom(...strings));
                rl.close(); // Закрываем интерфейс
            } else {
                // Добавляем введенную строку в массив и спрашиваем снова
                strings.push(input);
                askForInput();
            }
        });
    }

    askForInput(); // Начинаем запрашивать ввод
}

// Запускаем сбор строк
collectStrings();
