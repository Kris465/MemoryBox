const prompt = require('prompt-sync')();

function uniqueElements(arr1, arr2) {
    // Создаем множества для уникальных значений
    const set1 = new Set(arr1);
    const set2 = new Set(arr2);

    // Функция для нахождения уникальных элементов
    const uniqueInFirst = [...set1].filter(x => !set2.has(x));
    const uniqueInSecond = [...set2].filter(x => !set1.has(x));

    // Объединяем уникальные элементы из обоих массивов
    return [...uniqueInFirst, ...uniqueInSecond];
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
