const prompt = require('prompt-sync')();

function uniqueElements(arr1, arr2) {
    const uniqueArray = [];

    // Проверяем элементы первого массива
    for (let i = 0; i < arr1.length; i++) {
        let isUnique = true;
        for (let j = 0; j < arr2.length; j++) {
            if (arr1[i] === arr2[j]) {
                isUnique = false; // Элемент найден во втором массиве
                break;
            }
        }
        if (isUnique) {
            uniqueArray.push(arr1[i]); // Добавляем уникальный элемент
        }
    }

    // Проверяем элементы второго массива
    for (let i = 0; i < arr2.length; i++) {
        let isUnique = true;
        for (let j = 0; j < arr1.length; j++) {
            if (arr2[i] === arr1[j]) {
                isUnique = false; // Элемент найден в первом массиве
                break;
            }
        }
        if (isUnique) {
            uniqueArray.push(arr2[i]); // Добавляем уникальный элемент
        }
    }

    return uniqueArray;
}

// Ввод данных от пользователя
const input1 = prompt('Введите элементы первого массива через запятую: ');
const input2 = prompt('Введите элементы второго массива через запятую: ');

// Преобразуем ввод в массивы чисел
const array1 = input1.split(',').map(Number);
const array2 = input2.split(',').map(Number);

// Получаем результат
const result = uniqueElements(array1, array2);

// Выводим результат
console.log('Результат:', result);
