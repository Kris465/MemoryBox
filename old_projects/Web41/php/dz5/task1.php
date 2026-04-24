<?php
$array = [];
for ($i = 0; $i < 10; $i++) {
    $array[] = rand(1, 100);
}

echo "<h2>Исходный массив:</h2>";
echo implode(", ", $array);

$greaterThanPrevious = [];
for ($i = 1; $i < count($array); $i++) {
    if ($array[$i] > $array[$i - 1]) {
        $greaterThanPrevious[] = $array[$i];
    }
}

echo "<h2>Элементы, которые больше предыдущих:</h2>";
echo implode(", ", $greaterThanPrevious);

$sum = array_sum($array);
$average = $sum / count($array);

echo "<h2>Сумма всех элементов: $sum</h2>";
echo "<h2>Среднее значение: " . round($average, 2) . "</h2>";

$oddElements = array_filter($array, function($num) {
    return $num % 2 !== 0;
});

rsort($oddElements);

echo "<h2>Отсортированные нечетные элементы по убыванию:</h2>";
echo implode(", ", $oddElements);
?>