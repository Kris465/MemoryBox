<?php
$array = [
    ['type' => 'Agit', 'value' => 10],
    ['type' => 'B', 'value' => 20],
    ['type' => 'C', 'value' => 30],
    ['type' => 'D', 'value' => 40],
    ['type' => 'E', 'value' => 50],
    ['type' => 'F', 'value' => 60],
    ['type' => 'G', 'value' => 70],
    ['type' => 'H', 'value' => 80],
    ['type' => 'I', 'value' => 90],
    ['type' => 'J', 'value' => 100],
];

echo "<h2>Записи в массиве:</h2>";
foreach ($array as $element) {
    echo "Type: " . $element['type'] . ", Value: " . $element['value'] . "<br>";
}
?>