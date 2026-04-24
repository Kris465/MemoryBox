<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=`device-width`, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $initialDeposit = floatval($_POST['deposit']);
    $interestRate = 0.2; 
    $years = 20; 
    echo "<table border='1'>";
    echo "<tr><th>Год</th><th>Сумма</th><th>Прибыль</th></tr>";

    for ($year = 1; $year <= $years; $year++) {
        $amount = $initialDeposit * pow((1 + $interestRate), $year); 
        $profit = $amount - $initialDeposit; 

        echo "<tr>";
        echo "<td>$year</td>";
        echo "<td>" . round($amount, 2) . "</td>"; 
        echo "<td>" . round($profit, 2) . "</td>"; 
        echo "</tr>";
    }

    echo "</table>";
} else {

    echo '<form method="post" action="">
            <label for="deposit">Введите сумму депозита:</label>
            <input type="number" id="deposit" name="deposit" required>
            <input type="submit" value="Рассчитать">
          </form>';
}
?>
</body>
</html>
