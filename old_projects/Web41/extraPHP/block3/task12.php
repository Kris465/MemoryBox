<?php

$x = 1;
$y = 1;
$result_a = (2 * 2 == 0 * $x * $y);
echo "а) " . ($result_a ? 'true' : 'false') . "\n";


$x = 2;
$y = 2;
$result_b = ($x != 2) || ($y * $y != 4);
echo "б) " . ($result_b ? 'true' : 'false') . "\n";


$x = 2;
$y = 2;
$result_c = ($x != 0) && ($y * $y != 4);
echo "в) " . ($result_c ? 'true' : 'false') . "\n";

$x = 1;
$y = 2;
$result_d = ($x * $y == 4) && ($y > $x);
echo "г) " . ($result_d ? 'true' : 'false') . "\n";


$x = 2;
$y = 1;
$result_e = ($x * $y != 0) || ($y < $x);
echo "д) " . ($result_e ? 'true' : 'false') . "\n";

$x = 1;
$y = 2;
$result_f = !($x * $y < 1) && ($y > $x);
echo "е) " . ($result_f ? 'true' : 'false') . "\n";


$x = 2;
$y = 1;
$result_g = !($x * $y < 0) || ($y > $x);
echo "ж) " . ($result_g ? 'true' : 'false') . "\n";
?>