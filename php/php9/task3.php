<?php
/**
 * @param int
 * @param int 
 * @return string 
 */
function generateRandomDivs(int $count, int $total = 10): string {

    if ($count <= 0) {
        return '';
    }

    $left = rand(0, 80); 
    $top = rand(0, 80);  
    $color = sprintf('#%06X', rand(0, 0xFFFFFF));

    $currentDiv = sprintf(
        '<div id="div-%d" style="position: absolute; left: %d%%; top: %d%%; width: 50px; height: 50px; background-color: %s; border: 1px solid #000;"></div>',
        $total - $count + 1,
        $left,
        $top,
        $color
    );

    return $currentDiv . generateRandomDivs($count - 1, $total);
}

$divs = generateRandomDivs(10);
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>10 случайных DIV (рекурсивно)</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
        }
        .container {
            position: relative;
            width: 100%;
            height: 500px;
            border: 2px dashed #ccc;
            margin-bottom: 20px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .controls {
            text-align: center;
            margin: 20px 0;
        }
        button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>10 DIV со случайными координатами</h1>
    <div class="container">
        <?= $divs ?>
    </div>
    <div class="controls">
        <button onclick="window.location.reload()">Сгенерировать снова</button>
    </div>
</body>
</html>