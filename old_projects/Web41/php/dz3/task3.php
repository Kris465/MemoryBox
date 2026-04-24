<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
$diameter = 50; 
$color = 'blue'; 

echo '<div style="display: flex;">'; 
for ($i = 0; $i < 10; $i++) {
    echo '<div style="width: ' . $diameter . 'px; height: ' . $diameter . 'px; background-color: ' . $color . '; border-radius: 50%; margin: 5px;"></div>';
}
echo '</div>';
?>
</body>
</html>