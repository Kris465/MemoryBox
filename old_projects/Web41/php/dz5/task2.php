<?php
$dates = [
    '2023-01-01',
    '2023-02-15',
    '2023-03-10',
    '2023-04-05',
    '2023-05-20'
];
echo "<h2>Массив дат:</h2>";
foreach ($dates as $date) {
    echo $date . "<br>";
}
echo "<h2>Количество дней между соседними датами:</h2>";
for ($i = 0; $i < count($dates) - 1; $i++) {
    $date1 = new DateTime($dates[$i]);
    $date2 = new DateTime($dates[$i + 1]);
    $interval = $date1->diff($date2);
    echo "Между {$dates[$i]} и {$dates[$i + 1]}: " . $interval->days . " дней<br>";
}
?>