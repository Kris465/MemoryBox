<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Вывод действий</title>
</head>
<body>
    <h1>Введите первую и вторую переменную: </h1>
    <form method="POST" action="">
    <label for="data1">Первое значение:</label>
        <input type="number" id="data1" name="data1" required>
        <br>
        <label for="data2">Второе значение:</label>
        <input type="number" id="data2" name="data2" required>
        <br>
        <input type="submit" value="Отправить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $data1 = htmlspecialchars($_POST['data1']);
        $data2 = htmlspecialchars($_POST['data2']); 
        $rez = $data1 + $data2;

        echo "<h2>$data1 + $data2 = $rez</h2>";
    }
    ?>
</body>
</html>