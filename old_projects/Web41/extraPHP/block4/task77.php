<?php
$a = floatval(readline());
$b = floatval(readline());

$sqrtB = sqrt($b);

if ($sqrtB < $a) {
    $b *= 5;
}

echo $b;
?>