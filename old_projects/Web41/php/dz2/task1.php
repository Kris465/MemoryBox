<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Кратные ли переменные?</title>
</head>
<body>
<h1>Введите первую переменную и вторую: </h1>
    <form method="POST" action="">
        <label for="data">Первое значение:</label>
        <input type="text" id="data" name="data" required>
        <input type="submit" value="Отправить">

        <label for="data2">Второе значение:</label>
        <input type="number" id="data2" name="data2" required>
        <br>
        <input type="submit" value="Отправить">
    </form>

    <?php
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['firstNumber']) && isset($_POST['secondNumber'])) {
    $firstNumber = intval($_POST['firstNumber']);
    $secondNumber = intval($_POST['secondNumber']);

    if ($secondNumber != 0) {
        if ($firstNumber % $secondNumber == 0) {
            echo "<p>Число $firstNumber кратно числу $secondNumber.</p>";
        } else {
            echo "<p>Число $firstNumber не кратно числу $secondNumber.</p>";
        }
    } else {
        echo "<p>Деление на ноль невозможно.</p>";
    }
}
?>

</body>
</html>