<?php
function calculateY($a) {
    if (!is_numeric($a)) {
        return "Ошибка: Ввод должен быть числом.";
    }

    $numerator = pow($a, 2) + 10; 
    $denominator = sqrt(pow($a, 2) + 1); 

    if ($denominator == 0) {
        return "Ошибка: Деление на ноль.";
    }

    $y = $numerator / $denominator; 
    return $y; 
}

$a = isset($_GET['a']) ? $_GET['a'] : 0;

$result = calculateY($a);
echo "y = " . $result;
?>