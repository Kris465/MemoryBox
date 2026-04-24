<?php
$N = 10;

$oddNumbers = [];

for ($i = 0; $i < $N; $i++) {
    $oddNumbers[] = 2 * $i + 1;
}

$sum = array_sum($oddNumbers);
$average = $sum / count($oddNumbers);

$oddNumbersReversed = array_reverse($oddNumbers);

?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Нечетные числа</title>
    <style>
        .odd-number {
            color: red; 
            font-size: <?php echo max($oddNumbers) . 'px'; ?>;
        }
    </style>
</head>
<body>

<h2>Сгенерированные нечетные числа:</h2>
<ul>
    <?php foreach ($oddNumbersReversed as $number): ?>
        <li class="odd-number"><?php echo $number; ?></li>
    <?php endforeach; ?>
</ul>

<p>Среднее значение: <strong><?php echo $average; ?></strong></p>

</body>
</html>