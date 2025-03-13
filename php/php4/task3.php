<?php
function printMultiplicationTable($number) {
    for ($i = 1; $i <= 10; $i++) {
        echo "$number × $i = " . ($number * $i) . "<br>";
    }
}

for ($j = 2; $j <= 10; $j++) {
    echo "<h3>Таблица умножения на $j:</h3>";
    printMultiplicationTable($j);
    echo "<br>";
}
?>
