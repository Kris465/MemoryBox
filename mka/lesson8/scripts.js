document.getElementById('generateColorButton').addEventListener('click', function() {
    // Генерируем случайный цвет в формате HEX
    const randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
    
    // Изменяем цвет фона color-box
    document.getElementById('colorBox').style.backgroundColor = randomColor;

    // Обновляем текст с кодом цвета
    document.getElementById('colorCode').textContent = 'Цвет: ' + randomColor;
});
