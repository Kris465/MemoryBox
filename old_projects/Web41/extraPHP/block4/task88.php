<?php
function f($x) {
    if ($x <= 0) {
        return 0;
    } elseif ($x > 0 && $x <= 1) {
        return $x;
    } else {
        return $x * $x;
    }
}

$x = 2;
$result = f($x);
echo "f($x) = $result\n";
?>
