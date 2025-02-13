document.getElementById('generateColorButton').addEventListener('click', function() {
    const randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
    document.getElementById('colorBox').style.backgroundColor = randomColor;
    document.getElementById('colorCode').textContent = 'Цвет: ' + randomColor;
});
