const prompt = require('prompt-sync')();

function bubleSort(arr) {
    let n = arr.length;
    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                let temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    return arr;
}

function getArrayFromInput() {
    let input = prompt("Введите элементы массива через запятую: ");
    let array = input.split(',').map(num => parseFloat(num.trim()));
    return array;
}

let array = getArrayFromInput();
let sortedArray = bubleSort(array);
console.log("Отсортированный массив: ", sortedArray);