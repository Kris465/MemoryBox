document.getElementById('discountButton').addEventListener('click', function() {
    const purchaseAmount = Number(document.getElementById('discountInput').value);
    const discountResult = document.getElementById('discountResult');
    let discount = 0;

    if (purchaseAmount >= 200 && purchaseAmount < 300) {
        discount = 0.03;
    } else if (purchaseAmount >= 300 && purchaseAmount < 500) {
        discount = 0.05;
    } else if (purchaseAmount >= 500) {
        discount = 0.07;
    }

    const finalAmount = purchaseAmount * (1 - discount);
    discountResult.textContent = `Сумма к оплате со скидкой: ${finalAmount.toFixed(2)}`;
});
