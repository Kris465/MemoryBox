const prompt = require('prompt-sync')(); 

let shoppingList = [];

function displayShoppingList() {
    const sortedList = shoppingList.sort((a, b) => {
        return a.purchased - b.purchased;
    });

    sortedList.forEach(item => {
        const status = item.purchased ? "Куплено" : "Не куплено";
        console.log(`${item.productName} - ${item.quantity} (${status})`);
    });
}

function addPurchase(productName, quantity) {
    const existingItem = shoppingList.find(item => item.productName === productName);
    if (existingItem) {
        existingItem.quantity += quantity;
    } else {
        shoppingList.push({ productName, quantity, purchased: false });
    }
}

function purchaseProduct(productName) {
    const item = shoppingList.find(item => item.productName === productName);
    if (item) {
        item.purchased = true; 
    } else {
        console.log(`Продукт "${productName}" не найден в списке.`);
    }
}

addPurchase(prompt('Название продукта: '), prompt('Количество: '));
addPurchase(prompt('Название продукта: '), prompt('Количество: '));
addPurchase(prompt('Название продукта: '), prompt('Количество: '));
//addPurchase("Бананы", 2);
//addPurchase("Молоко", 1);

console.log("Список покупок:");
displayShoppingList(); 

const pays = prompt('Введите купленный продукт: ');

purchaseProduct(pays);
console.log("\nОбновленный список покупок:");
displayShoppingList(); 

