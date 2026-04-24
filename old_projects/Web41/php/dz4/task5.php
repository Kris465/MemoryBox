<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=
    , initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $number = $_POST['number']; 
    $reversedNumber = strrev($number); 

    echo "<h2>Число задом наперед: $reversedNumber</h2>";
} else {
    
    echo '<form method="post" action="">
            <label for="number">Введите число:</label>
            <input type="text" id="number" name="number" required>
            <input type="submit" value="Показать задом наперед">
          </form>';
}
?>
</body>
</html>