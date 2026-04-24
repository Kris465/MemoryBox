TODO
<!-- Если нужно поддерживать числа с плавающей точкой, добавьте проверку с помощью filter_var() с флагом FILTER_VALIDATE_FLOAT.
Если приложение будет использоваться в разных регионах, учтите, что в некоторых локалях десятичный разделитель — запятая (например, 1,23 вместо 1.23).
Если нужно сделать форму более динамичной, можно добавить обработку данных через AJAX без перезагрузки страницы. -->


<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $number = $_POST['number'];

    echo "Вы ввели число: $number";
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Ввод числа</title>
</head>
<body>
    <form method="post">
        <label for="number">Введите число:</label>
        <input type="text" id="number" name="number" required>
        <br>
        <input type="submit" value="Отправить">
    </form>
</body>
</html>