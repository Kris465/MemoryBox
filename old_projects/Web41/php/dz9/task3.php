<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Случайные div с координатами</title>
    <style>
        .random-div {
            position: absolute;
            width: 100px;
            height: 100px;
            background-color: rgba(0, 150, 255, 0.5);
            border: 1px solid #000;
        }
    </style>
</head>
<body>

<?php
function generateDivs($count) {
    if ($count <= 0) {
        return; 
    }

    $x = rand(0, 90); 
    $y = rand(0, 90);

    echo "<div class='random-div' style='left: {$x}%; top: {$y}%;'></div>";

    generateDivs($count - 1);
}
generateDivs(10);
?>

</body>
</html>