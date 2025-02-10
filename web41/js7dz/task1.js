const prompt = require('prompt-sync')();

let shoppingList = [];

function displayList() {
    const notPurchased = shoppingList.filter(item => !item.purchased);
    const purchased = shoppingList.filter(item => item.purchased);
    
    console.log("Список покупок:");
    notPurchased.forEach(item => {
        console.log(`- ${item.name}: ${item.quantity} (не куплено)`);
    });
    purchased.forEach(item => {
        console.log(`- ${item.name}: ${item.quantity} (куплено)`);
    });
}

function addPurchase(name, quantity) {
    const existingItem = shoppingList.find(item => item.name === name);
    if (existingItem) {
        existingItem.quantity += quantity;
    } else {
        shoppingList.push({ name, quantity, purchased: false });
    }
}

// Функция для покупки продукта
function purchaseProduct(name) {
    const item = shoppingList.find(item => item.name === name);
    if (item) {
        item.purchased = true;
    } else {
        console.log(`Продукт "${name}" не найден в списке.`);
    }
}

while (true) {
    console.log("\nВыберите действие:");
    console.log("1. Вывести список покупок");
    console.log("2. Добавить покупку");
    console.log("3. Купить продукт");
    console.log("4. Выйти");

    const choice = prompt("Ваш выбор: ");

    switch (choice) {
        case '1':
            displayList();
            break;
        case '2':
            const nameToAdd = prompt("Введите название продукта: ");
            const quantityToAdd = parseInt(prompt("Введите количество: "), 10);
            addPurchase(nameToAdd, quantityToAdd);
            break;
        case '3':
            const nameToPurchase = prompt("Введите название купленного продукта: ");
            purchaseProduct(nameToPurchase);
            break;
        case '4':
            console.log("Выход из программы...");
            process.exit();
            break;
        default:
            console.log("Неверный выбор. Пожалуйста, попробуйте снова.");
    }
}
