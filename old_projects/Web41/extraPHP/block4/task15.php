<?php
$birthYear = 1990;
$birthMonth = 5;
$currentYear = 2023;
$currentMonth = 8;

$age = $currentYear - $birthYear;

if ($birthMonth > $currentMonth) {
    $age--;
} elseif ($birthMonth == $currentMonth) {
    
}
echo "Возраст человека: " . $age . " полных лет.\n";
?>