<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php


$a = 5.8;
$b = 0; 
$b = $a; 
$a = $b; 
$b = 7.9; 

echo "а) a = " . $a . ", b = " . $b . "\n"; 


$a = 0;
$b = 9.99;
$b = $a; 
$a = $b; 

echo "б) a = " . $a . ", b = " . $b . "\n"; 

?>
</body>
</html>