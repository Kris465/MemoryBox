# Таблицы

▎Таблицы

Таблицы в HTML используются для представления данных в виде строк и столбцов. Они позволяют организовать информацию в структурированном виде, что делает ее более понятной и доступной для восприятия.

▎Создание простейшей таблицы

Для создания таблицы в HTML используется тег ```<table>```. Внутри него размещаются строки с помощью тега ```<tr>``` (table row), а ячейки с помощью тегов ```<td>``` (table data) для обычных ячеек и ```<th>``` (table header) для заголовков.

Пример простейшей таблицы:
```html
<table>
    <tr>
        <th>Имя</th>
        <th>Возраст</th>
    </tr>
    <tr>
        <td>Иван</td>
        <td>25</td>
    </tr>
    <tr>
        <td>Мария</td>
        <td>30</td>
    </tr>
</table>
```
▎Объединение ячеек: атрибуты colspan, rowspan

Атрибуты colspan и rowspan используются для объединения ячеек в таблицах. 

• colspan позволяет объединить несколько ячеек в одну по горизонтали.

• rowspan позволяет объединить несколько ячеек в одну по вертикали.

Пример:
```html
<table>
    <tr>
        <th rowspan="2">Имя</th>
        <th colspan="2">Возраст</th>
    </tr>
    <tr>
        <th>Год</th>
        <th>Месяц</th>
    </tr>
    <tr>
        <td>Иван</td>
        <td>25</td>
        <td>6</td>
    </tr>
</table>
```

▎Тег заголовка: <caption>. Теги логического группирования столбцов: <colgroup>, <col>

Тег <caption> используется для добавления заголовка к таблице, что помогает пользователю понять, о чем идет речь. 

Теги <colgroup> и <col> используются для логического группирования столбцов. Это может быть полезно для применения стилей к группе столбцов.

Пример:

```html
<table>
    <caption>Список пользователей</caption>
    <colgroup>
        <col style="background-color: #f2f2f2">
        <col style="background-color: #ffffff">
    </colgroup>
    <tr>
        <th>Имя</th>
        <th>Возраст</th>
    </tr>
    <!-- строки таблицы -->
</table>
```

▎Теги логического структурирования таблиц: <thead>, <tbody>, <tfoot>

Эти теги помогают структурировать таблицу на логические части:

• <thead> — содержит заголовки таблицы.

• <tbody> — основное содержимое таблицы.

• <tfoot> — содержит итоговые данные или подведение итогов.

Пример:
```html
<table>
    <thead>
        <tr>
            <th>Имя</th>
            <th>Возраст</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Иван</td>
            <td>25</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <td colspan="2">Итого: 1 человек</td>
        </tr>
    </tfoot>
</table>
```
▎Управление рамками таблицы

Управление рамками таблицы осуществляется с помощью атрибута border или CSS. Атрибут border задает толщину рамки, а CSS позволяет более гибко настраивать внешний вид.

Пример с использованием CSS:
```html
<table style="border-collapse: collapse; border: 1px solid black;">
    <tr style="border: 1px solid black;">
        <td style="border: 1px solid black;">Ячейка 1</td>
        <td style="border: 1px solid black;">Ячейка 2</td>
    </tr>
</table>
```
▎Практика: создание сложных таблиц

На практике можно создавать более сложные таблицы, комбинируя вышеупомянутые элементы и атрибуты. Это может включать объединение ячеек, использование различных стилей и структурирование данных.

▎Табличная верстка — что это и почему не используется в современном стандарте?

Табличная верстка — это использование таблиц для структурирования страницы, а не только для представления данных. Это подход был популярен в ранних версиях HTML, но сейчас считается плохой практикой, так как:

1. Усложняет код и делает его менее доступным.

2. Плохо влияет на SEO.

3. Усложняет адаптацию под мобильные устройства.

Современные стандарты рекомендуют использовать CSS для верстки страниц, что позволяет создавать более гибкие и доступные макеты.

## Пример стилизованной таблицы с файлом стилей

```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>Стилизованная таблица</title>
</head>
<body>
    <div class="table-container">
        <table>
            <thead>
                <tr>
                    <th>Имя</th>
                    <th>Возраст</th>
                    <th>Город</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Иван</td>
                    <td>25</td>
                    <td>Москва</td>
                </tr>
                <tr>
                    <td>Анна</td>
                    <td>30</td>
                    <td>Санкт-Петербург</td>
                </tr>
                <tr>
                    <td>Петр</td>
                    <td>22</td>
                    <td>Екатеринбург</td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>
```

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
}

.table-container {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

table {
    width: 100%;
    border-collapse: collapse;
    background-image: url('background.jpg'); /* Замените 'background.jpg' на ваш путь к изображению */
    background-size: cover;
}

th, td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

th {
    background-color: #4CAF50; /* Цвет фона заголовков */
    color: white; /* Цвет текста заголовков */
}

tr:nth-child(even) {
    background-color: #f2f2f2; /* Цвет фона четных строк */
}

tr:hover {
    background-color: #ddd; /* Цвет фона строки при наведении */
}

@media (max-width: 600px) {
    th, td {
        padding: 8px;
        font-size: 14px;
    }
}
```
