const prompt = require('prompt-sync')();

let receipt = [];

function addItem(name, quantity, price) {
    receipt.push({ name, quantity, price });
}

function printReceipt() {
    console.log("\nЧек:");
    receipt.forEach(item => {
        const totalPrice = item.quantity * item.price;
        console.log(`${item.name} - ${item.quantity} шт. по ${item.price.toFixed(2)} руб. = ${totalPrice.toFixed(2)} руб.`);
    });
}

function calculateTotal() {
    return receipt.reduce((total, item) => total + (item.quantity * item.price), 0);
}

function getMostExpensiveItem() {
    return receipt.reduce((maxItem, item) => {
        const totalPrice = item.quantity * item.price;
        return totalPrice > (maxItem.total || 0) ? { name: item.name, total: totalPrice } : maxItem;
    }, {});
}

function calculateAveragePrice() {
    const totalItems = receipt.reduce((count, item) => count + item.quantity, 0);
    const totalPrice = calculateTotal();
    return totalItems > 0 ? totalPrice / totalItems : 0;
}

while (true) {
    console.log("\nВыберите действие:");
    console.log("1. Добавить товар в чек");
    console.log("2. Распечатать чек");
    console.log("3. Подсчитать общую сумму покупки");
    console.log("4. Найти самую дорогую покупку");
    console.log("5. Подсчитать среднюю стоимость одного товара");
    console.log("6. Выйти");

    const choice = prompt("Ваш выбор: ");

    switch (choice) {
        case '1':
            const name = prompt("Введите название товара: ");
            const quantity = parseInt(prompt("Введите количество: "), 10);
            const price = parseFloat(prompt("Введите цену за единицу: "));
            addItem(name, quantity, price);
            break;
        case '2':
            printReceipt();
            break;
        case '3':
            const total = calculateTotal();
            console.log(`Общая сумма покупки: ${total.toFixed(2)} руб.`);
            break;
        case '4':
            const mostExpensive = getMostExpensiveItem();
            if (mostExpensive.name) {
                console.log(`Самая дорогая покупка: ${mostExpensive.name} на сумму ${mostExpensive.total.toFixed(2)} руб.`);
            } else {
                console.log("Чек пуст.");
            }
            break;
        case '5':
            const averagePrice = calculateAveragePrice();
            console.log(`Средняя стоимость одного товара: ${averagePrice.toFixed(2)} руб.`);
            break;
        case '6':
            console.log("Выход из программы...");
            process.exit();
            break;
        default:
            console.log("Неверный выбор. Пожалуйста, попробуйте снова.");
    }
}