<?php
$x = (float)readline();

if ($x <= 0) {
    $f = 0;
} elseif ($x > 0 && $x < 1) {
    $f = $x;
} else {
    $f = $x * $x;
}

echo $f;
?>