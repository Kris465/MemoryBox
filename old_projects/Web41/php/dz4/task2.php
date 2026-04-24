<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Таблица умножения</title>
    <style>
        table {
            border-collapse: collapse;
            width: 30%;
            margin: 20px;
            float: left; 
        }
        th, td {
            border: 1px solid #000;
            padding: 10px;
            text-align: center;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>

<h1 style="text-align: center;">Таблица умножения от 2 до 10</h1>

<?php

for ($i = 2; $i <= 10; $i++) {
    echo "<table>";
    echo "<tr><th>Умножение на $i</th></tr>"; 
    for ($j = 1; $j <= 10; $j++) {
        $result = $i * $j;
        echo "<tr><td>$i × $j = $result</td></tr>"; 
    }
    echo "</table>";
}
?>

</body>
</html>