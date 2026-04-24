<?php
$initialAmount = 300;
$annualInterestRate = 20;
$years = 20;
echo "<table border='1'>";
echo "<tr><th>Год</th><th>Сумма на депозите</th><th>Прибыль за год</th></tr>";
$currentAmount = $initialAmount;

for ($year = 1; $year <= $years; $year++) {
    $profit = $currentAmount * ($annualInterestRate / 100);
    $currentAmount += $profit;
    echo "<tr>";
    echo "<td>$year</td>";
    echo "<td>" . number_format($currentAmount, 2) . "</td>";
    echo "<td>" . number_format($profit, 2) . "</td>";
    echo "</tr>";
}

echo "</table>";
?>