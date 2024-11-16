const prompt = require('prompt-sync')();

function bubbleSort(arr) {
    let n = arr.length;
    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            // Сравниваем соседние элементы
            if (arr[j] > arr[j + 1]) {
                // Меняем их местами, если они в неправильном порядке
                let temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    return arr;
}

function getArrayFromInput() {
    let input = prompt("Введите элементы массива, разделенные запятой: ");
    // Преобразуем строку в массив чисел
    let array = input.split(',').map(num => parseFloat(num.trim()));
    return array;
}

// Получаем массив от пользователя
let array = getArrayFromInput();

// Сортируем массив
let sortedArray = bubbleSort(array);
console.log("Отсортированный массив:", sortedArray);
