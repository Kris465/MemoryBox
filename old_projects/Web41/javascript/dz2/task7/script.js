document.getElementById('discountButton').addEventListener('click', function() {
    const symma = Number(document.getElementById('discountInput').value);
    const discountResult = document.getElementById('discountResult');
    const discount = 0;

    if (symma >= 200 && symma < 300){
        discount = 0.03;
    } else if (symma >= 300 && symma < 500){
        discount = 0.05;
    } else if (symma >= 500){
        discount = 0.07;
    } 
    
    const finalSymma = symma * (1 - discount);
    discountResult.textContent(`сумма к оплате со скидкой ${finalSymma.toFixed(2)}`);
});