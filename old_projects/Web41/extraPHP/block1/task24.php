<?php
function calculateY($x, $a) {
    $num = $x * pow($a, 2) * sin(3);
    $denom = 3.56 * 2 * 10 * 1; 

    if ($denom == 0) {
        return "Ошибка: Деление на ноль.";
    }

    $y = $num / $denom;
    return $y; 
}

function calculateZ($x) {
    if ($x == 0) {
        return "Ошибка: Деление на ноль.";
    }

    $z = (3.2 * sin(5)) / $x; 
    return $z; 
}

$x = isset($_GET['x']) ? floatval($_GET['x']) : 1;
$a = isset($_GET['a']) ? floatval($_GET['a']) : 1;

$resultY = calculateY($x, $a);
$resultZ = calculateZ($x);

echo "Результат функции Y: " . $resultY . "<br>";
echo "Результат функции Z: " . $resultZ . "<br>";
?>