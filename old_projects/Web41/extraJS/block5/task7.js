const pricePerItem = 20.4;

for (let quantity = 2; quantity <= 20; quantity++) {
    const totalCost = (pricePerItem * quantity).toFixed(2);
    console.log(`${quantity} шт. - ${totalCost} руб.`);
}