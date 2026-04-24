<?php
function generateRandomColor() {
    $red = dechex(rand(0, 255));
    $green = dechex(rand(0, 255));
    $blue = dechex(rand(0, 255));

    $red = str_pad($red, 2, '0', STR_PAD_LEFT);
    $green = str_pad($green, 2, '0', STR_PAD_LEFT);
    $blue = str_pad($blue, 2, '0', STR_PAD_LEFT);

    return '#' . $red . $green . $blue;
}

$randomColor = generateRandomColor();
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Случайный цвет</title>
    <style>
        .color-box {
            width: 200px; 
            height: 200px; 
            display: flex;
            align-items: center;
            justify-content: center;
            color: white; 
            font-size: 24px; 
            border: 1px solid #000; 
        }
    </style>
</head>
<body>

<div class="color-box" style="background-color: <?php echo $randomColor; ?>;">
    <?php echo $randomColor; ?>
</div>

</body>
</html>