<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Рисование div</title>
    <style>
        .rectangle {
            position: absolute; 
            width: 100px; 
            height: 100px;
        }
    </style>
</head>
<body>

<?php

$x = 150; 
$y = 100; 
$color = "red"; 


$screenWidth = 1920; 
$screenHeight = 1080; 


if ($x >= 0 && $y >= 0 && $x + 100 <= $screenWidth && $y + 100 <= $screenHeight) {

    echo "<div class='rectangle' style='left: {$x}px; top: {$y}px; background-color: {$color};'></div>";
} else {

    echo "<p>Координаты находятся за пределами экрана!</p>";
}
?>

</body>
</html>