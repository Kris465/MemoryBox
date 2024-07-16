# Tic-Tac-Toe
## Игра в крестики - нолики

Задача 1:  Возьмите из общей папки шаблон index.html. Откройте его в vs code. Выглядит он так:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Заголовок страницы</title>
</head>
<body>
    <header>
        <h1>Заголовок страницы</h1>
    </header>

    <div> …
    </div>
</body>
</html>
```

Задача 2: Назовите страницу внутри тега title.   <title>Крестики - нолики </title>

Задача 3: Внутри тега h1, введите название игры. <h1>Игра в крестики - нолики </h1>

Задача 4: Внутри тега div создайте поле для игры в крестики-нолики: 

```html
    <div class="game-board">
        <div class="row">
            <div class="cell" data-cell></div>
            <div class="cell" data-cell></div>
            <div class="cell" data-cell></div>
        </div>
        <div class="row">
            <div class="cell" data-cell></div>
            <div class="cell" data-cell></div>
            <div class="cell" data-cell></div>
        </div>
        <div class="row">
            <div class="cell" data-cell></div>
            <div class="cell" data-cell></div>
            <div class="cell" data-cell></div>
        </div>
    </div>
```

Задача 5: После этого блока кода создайте новый тег для JavaScript с тем же отступом что и у тега div:

```html
<script src="script.js"></script>
```

Задача 6: Создайте новый файл. Назовите его styles.css. После тега <title>Крестики - нолики </title> вставьте тег – ссылку на стили с тем же отступом, что и тег title: 

```html
<link rel="stylesheet" href="styles.css">
```

Задача 7: Запустите и посмотрите на страницу в браузере. Разместите заголовок по центру. Откройте в vs code файл styles.css и задайте параметр для заголовка: 

```css
h1 {
    text-align: center;
}
```

Задача 8: Запустите страницу и убедитесь, что все получилось. Задайте цвет и стиль для текста на фоне (по умолчанию, если такой предполагается), добавив строчки в styles.css:

```css
body {
    background-color: #2598e5; /* Цвет фона страницы */
    font-family: Arial, sans-serif;   
}
```

Задача 9: Задайте стиль для игральной доски (для общей формы, цвет и размер ячеек) в файле styles.css: 

```css
.game-board {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
}

.row {
    display: flex;
}

.cell {
    width: 100px;
    height: 100px;
    background-color: lightgray;
    border: 1px solid black;
}
```

Задача 10: Задайте цвет отмеченных ячеек, для крестика и для нолика в styles.css:

```css
.cell.x {
    background-color: blue;
}

.cell.o {
    background-color: red;
}
```

Задача 11: Создайте файл script.js. Откройте его в vs code и создайте глобальный селектор, внутри которого мы будем писать функции игры:

```JavaScript
document.addEventListener('DOMContentLoaded', () => {
    const X_CLASS = 'x';
    const O_CLASS = 'o';
    let currentPlayer = X_CLASS;
    const cellElements = document.querySelectorAll('.cell');

Задача 12: С отступом предыдущих строк создаем цикл игры:

    cellElements.forEach(cell => {
        cell.addEventListener('click', handleClick, { once: true });
    });
```

Задача 13: Как видите, в предыдущую функцию мы передаем другую функцию, которая обрабатывает клик по клетке поля. Давайте напишем ее. С тем же отступом:

```javascript
    function handleClick(e) {
        const cell = e.target;
        if (cell.classList.contains(X_CLASS) || cell.classList.contains(O_CLASS)) {
            return; // Чтобы игровое поле не перезаполнялось, если ячейка уже занята
        }
        const currentClass = currentPlayer === X_CLASS ? X_CLASS : O_CLASS;
        placeMark(cell, currentClass);
        if (checkWin(currentClass)) {
            alert(`${currentClass === X_CLASS ? 'X' : 'O'} wins!`);
        } else if (isDraw()) {
            alert(`It's a draw!`);
        } else {
            currentPlayer = currentPlayer === X_CLASS ? O_CLASS : X_CLASS;
        }
    }
```

Задача 14: Теперь напишем результат нашего клика, и что происходит после того, как мы нажали на ячейку поля, с тем же отступом:

```javascript
    function placeMark(cell, currentClass) {
        cell.classList.add(currentClass);
    }
```

Задача 15: Мы уже почти написали весь функционал игры, осталось определить победителя! Для этого с тем же отступом определим комбинации для победы, сохраним в переменную-константу и напишем функцию:

```javascript
    const WINNING_COMBINATIONS = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Горизонтальные линии
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Вертикальные линии
        [0, 4, 8], [2, 4, 6] // Диагонали
    ];

    function checkWin(currentClass) {
        return WINNING_COMBINATIONS.some(combination => {
            return combination.every(index => {
                return cellElements[index].classList.contains(currentClass);
            });
        });
    }
```

Задача 16: И завершающий этап! Заставим наш движок отрисовывать игровое поле!

```javascript
    function isDraw() {
        return [...cellElements].every(cell => {
            return cell.classList.contains(X_CLASS) || cell.classList.contains(O_CLASS);
        });
    }
});
```
