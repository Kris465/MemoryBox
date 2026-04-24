<?php
$x = (float)readline();

if ($x < -1) {
    $y = -1;
} elseif ($x > -1) {
    $y = $x;
} else { 
    $y = 1;
}

echo $y;
?>