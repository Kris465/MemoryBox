<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Генерация случайного массива</title>
</head>
<body>

<h1>Генерация случайного массива</h1>
<form method="post">
    <label for="count_elem">Количество элементов:</label>
    <input type="number" id="count_elem" name="count_elem" required><br><br>

    <label for="min_val">Минимальное значение:</label>
    <input type="number" id="min_val" name="min_val" required><br><br>

    <label for="max_val">Максимальное значение:</label>
    <input type="number" id="max_val" name="max_val" required><br><br>

    <input type="submit" value="Сгенерировать">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $count_elem = intval($_POST['count_elem']);
    $min_val = intval($_POST['min_val']);
    $max_val = intval($_POST['max_val']);


    generateRandomArray($count_elem, $min_val, $max_val);
}

function generateRandomArray($count_elem, $min_val, $max_val) {

    if ($min_val > $max_val) {
        list($min_val, $max_val) = array($max_val, $min_val);
    }


    $randomArray = [];


    for ($i = 0; $i < $count_elem; $i++) {
        $randomArray[] = rand($min_val, $max_val);
    }


    echo "<h2>Результаты:</h2>";
    echo "Count: $count_elem<br>";
    echo "Min: $min_val<br>";
    echo "Max: $max_val<br>";
    echo "Output: " . implode(", ", $randomArray) . "<br>";
}
?>

</body>
</html>