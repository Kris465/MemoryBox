<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Рисование фигур</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Рисование фигур</h1>
        <form id="shapeForm" onsubmit="return validateForm()">
            <label for="shape">Выберите фигуру:</label>
            <select id="shape" name="shape">
                <option value="circle">Круг</option>
                <option value="square">Квадрат</option>
                <option value="triangle">Треугольник</option>
            </select>
            <label for="x">Координата X:</label>
            <input type="number" id="x" name="x" required>
            <label for="y">Координата Y:</label>
            <input type="number" id="y" name="y" required>
            <label for="color">Цвет:</label>
            <input type="color" id="color" name="color" required>
            <button type="submit">Нарисовать</button>
        </form>
        <div id="canvas"></div>
        <div id="message"></div>
    </div>
    <script src="script.js"></script>
</body>
</html>
