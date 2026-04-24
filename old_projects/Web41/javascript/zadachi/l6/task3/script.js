const list = {
    values: ['Яблоко', 'Банан', 'Апельсин'],
    
    printList() {
        const productListDiv = document.getElementById('productList');
        productListDiv.innerHTML = '';
        const sortedValues = this.values.slice().sort();
        const ol = document.createElement('ol');
        sortedValues.forEach(value => {
            const li = document.createElement('li');
            li.textContent = value;
            ol.appendChild(li);
        });
        
        productListDiv.appendChild(ol);
    },

    add(product) {
        this.values.push(product);
        this.printList();
    }
};

list.printList();

document.getElementById('addButton').addEventListener('click', () => {
    const productInput = document.getElementById('productInput');
    const newProduct = productInput.value.trim();
    
    if (newProduct) {
        list.add(newProduct);
        productInput.value = '';
    } else {
        alert('Пожалуйста, введите название продукта.');
    }
});


setTimeout(() => {
    list.values = ['Молоко', 'Хлеб', 'Яйца', 'Сыр'];
    list.printList();
}, 10000);