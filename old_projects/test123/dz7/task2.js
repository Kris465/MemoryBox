const prompt = require('prompt-sync')(); 


const receipt = [
    { name: "Яблоки", quantity: 3, price: 50 },
    { name: "Хлеб", quantity: 2, price: 30 },
    { name: "Молоко", quantity: 1, price: 60 },
    { name: "Сыр", quantity: 1, price: 120 }
];

function printReceipt(receipt) {
    console.log("Чек:");
    receipt.forEach(item => {
        console.log(`${item.name} (количество: ${item.quantity}, цена за единицу: ${item.price} руб.)`);
    });
}

function calculateTotal(receipt) {
    return receipt.reduce((total, item) => total + (item.quantity * item.price), 0);
}

function getMostExpensiveItem(receipt) {
    return receipt.reduce((mostExpensive, item) => {
        const itemTotal = item.quantity * item.price;
        return itemTotal > mostExpensive.total ? { item, total: itemTotal } : mostExpensive;
    }, { item: null, total: 0 }).item;
}

function calculateAveragePrice(receipt) {
    const totalItems = receipt.reduce((total, item) => total + item.quantity, 0);
    const totalCost = calculateTotal(receipt);
    return totalItems ? (totalCost / totalItems).toFixed(2) : 0;
}

printReceipt(receipt);
console.log(`Общая сумма покупки: ${calculateTotal(receipt)} руб.`);
const mostExpensiveItem = getMostExpensiveItem(receipt);
console.log(`Самая дорогая покупка: ${mostExpensiveItem.name} (количество: ${mostExpensiveItem.quantity}, цена за единицу: ${mostExpensiveItem.price} руб.)`);
console.log(`Средняя стоимость одного товара: ${calculateAveragePrice(receipt)} руб.`);
