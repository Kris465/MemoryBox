<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php

$s = 14;
$s = 3;
$s = 1;
$s = 2;
$k = $s; 
$d = $s; 
$s = $d; 
$s = $d; 
$k = $s; 

echo "После группы а: s = $s, k = $k, d = $d\n";

$s = 0;
$k = 30;
$d = 5;
$k = 2;
$k = 100;
$s = $k; 
$d = $k; 
$k = $d; 
$d = $s; 
$s = $k; 

echo "После группы б: s = $s, k = $k, d = $d\n";
?>
</body>
</html>