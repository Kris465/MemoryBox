<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php

function calculate_y($x) {
  return 7 * pow($x, 2) - $x + 3 / 6;
}

function calculate_x($a) {
    if ($a == 0) {
        return "Деление на ноль невозможно";
    }
  return ($a + 12) / (2 * pow($a, 2));
}

$x_value = 2; 
$a_value = 4; 

$y_result = calculate_y($x_value);
$x_result = calculate_x($a_value);

echo "а) y = " . $y_result . " при x = " . $x_value . "\n";
echo "б) x = " . $x_result . " при a = " . $a_value . "\n";

?>
</body>
</html>