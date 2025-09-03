<?php
/**
 * @return string
 */
function generateRandomColor(): string {
    $red = str_pad(dechex(mt_rand(0, 255)), 2, '0', STR_PAD_LEFT);
    $green = str_pad(dechex(mt_rand(0, 255)), 2, '0', STR_PAD_LEFT);
    $blue = str_pad(dechex(mt_rand(0, 255)), 2, '0', STR_PAD_LEFT);

    return '#' . $red . $green . $blue;
}

$randomColor = generateRandomColor();
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Генератор случайных цветов</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            text-align: center;
        }
        .color-info {
            margin: 20px 0;
            padding: 15px;
            background: #f5f5f5;
            border-radius: 5px;
        }
        .color-box {
            width: 200px;
            height: 200px;
            margin: 20px auto;
            border: 2px solid #333;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        button {
            background: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
            transition: background 0.3s;
        }
        button:hover {
            background: #45a049;
        }
    </style>
</head>
<body>
    <h1>Генератор случайных цветов</h1>
    <div class="color-info">
        <p>Сгенерированный цвет: <strong><?= htmlspecialchars($randomColor) ?></strong></p>
    </div>
    <div class="color-box" style="background-color: <?= htmlspecialchars($randomColor) ?>;"></div>
    <form method="POST">
        <button type="submit">Сгенерировать новый цвет</button>
    </form>
    <div style="margin-top: 30px; font-size: 0.9em; color: #666;">
        <p>Функция генерирует случайный цвет в формате HEX (#RRGGBB), где:</p>
        <ul style="list-style-type: none; padding: 0;">
            <li>RR - красный компонент (00-FF)</li>
            <li>GG - зеленый компонент (00-FF)</li>
            <li>BB - синий компонент (00-FF)</li>
        </ul>
    </div>
</body>
</html>