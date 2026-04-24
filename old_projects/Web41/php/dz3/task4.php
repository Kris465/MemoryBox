<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Перевод из двоичной в шестнадцатеричную систему</title>
</head>
<body>

<h2>Перевод из двоичной в шестнадцатеричную систему счисления</h2>
<form method="post">
    <label for="binary">Введите двоичное число:</label>
    <input type="text" id="binary" name="binary" required>
    <input type="submit" value="Перевести">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    $binary = $_POST['binary'];

    
    if (preg_match('/^[01]+$/', $binary)) {
      
        $decimal = bindec($binary);
        
      
        $hexadecimal = dechex($decimal);
        
     
        echo "<p>Шестнадцатеричное представление числа $binary: $hexadecimal</p>";
    } else {
        echo "<p style='color:red;'>Пожалуйста, введите корректное двоичное число.</p>";
    }
}
?>

</body>