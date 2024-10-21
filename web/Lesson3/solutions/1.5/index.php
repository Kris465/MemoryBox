<?php
// Определяем переменные
$tag = 'div'; // Можно изменить на любой другой тег
$background_color = 'lightblue';
$color = 'darkblue';
$width = '300px';
$height = '100px';
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Динамический тег</title>
    <link rel="stylesheet" href="styles.css"> <!-- Подключаем CSS файл -->
</head>
<body>

<?php
// Выводим тег с заданными стилями
echo "<$tag style='background-color: $background_color; color: $color; width: $width; height: $height;'>Hello, World!</$tag>";
?>

<script src="script.js"></script> <!-- Подключаем JS файл -->
</body>
</html>
