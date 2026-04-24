<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
$a = intval(readline("Введите первое целое число (a): "));
$b = intval(readline("Введите второе целое число (b): "));

$result = ($b !== 0 && $a % $b == 0) || ($a !== 0 && $b % $a == 0) ? 1 : 42; 

echo $result . PHP_EOL;
?>

</body>
</html>