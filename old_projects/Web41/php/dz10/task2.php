<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Возведение в степень</title>
</head>
<body>

<h1>Возведение числа в степень</h1>
<form method="post">
    <label for="base">Число:</label>
    <input type="number" id="base" name="base" required><br><br>

    <label for="exponent">Степень:</label>
    <input type="number" id="exponent" name="exponent" required><br><br>

    <input type="submit" value="Вычислить">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
   
    $base = floatval($_POST['base']);
    $exponent = intval($_POST['exponent']);

   
    $result = power($base, $exponent);

 
    echo "<h2>Результат:</h2>";
    echo "$base в степени $exponent равно $result";
}

function power($base, $exponent) {
    return pow($base, $exponent);
}
?>

</body>
</html>