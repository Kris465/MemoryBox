const prompt = require('prompt-sync')();

let shoppingList = [];

function displayShoppingList() {
    const sortedList = shoppingList.sort((name, amount) => {
        return name.purchased - amount.purchased;
    });

    sortedList.forEach(item => {
        const status = item.purchased ? "Куплено" : "Не куплено";
        console.log(`${item.productName} - ${item.quantity} (${status})`);
    });
}

function addPurchase(productName, quantity) {
    const existingItem = shoppingList.find(item => item.productName === productName);
    if (existingItem) {
        existingItem.quantity += quantity ;
    } else {
        shoppingList.push( {
            productName, quantity, purchased: false
        });
    }
}

function purchaseProduct (productName) {
    const item = shoppingList.find(item => item.productName === productName);
    if (item) {
        item.purchased = true;
    } else {
        console.log(`Продукт "${productName}" не найден в списке.`);
    }
}

addPurchase(prompt('Название: '), prompt('Кол-во.: '));
addPurchase(prompt('Название: '), prompt('Кол-во.: '));
addPurchase(prompt('Название: '), prompt('Кол-во.: '));

console.log('Список покупок:');
displayShoppingList();

const pays = prompt('Введите купленный продукт: ');

purchaseProduct(pays);
console.log('\nОбновленный список покупок: ');
displayShoppingList();