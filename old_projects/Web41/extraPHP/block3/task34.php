<?php
$a = 3;
$b = 2;
$c = 5;
$d = 4;

$condition_a = ($a == $c) || ($b == $d);
$condition_b = abs($a - $c) == abs($b - $d);
$condition_c = (abs($a - $c) <= 1) && (abs($b - $d) <= 1);
$condition_g = (($a == $c) || ($b == $d)) || (abs($a - $c) == abs($b - $d));
$white_pawn_move = ($a == $c) && ($b + 1 == $d);
$white_pawn_capture = (abs($a - $c) == 1) && ($b + 1 == $d);
$condition_d = $white_pawn_move || $white_pawn_capture;
$black_pawn_move = ($a == $c) && ($b - 1 == $d);
$black_pawn_capture = (abs($a - $c) == 1) && ($b - 1 == $d);
$condition_e = $black_pawn_move || $black_pawn_capture;
$condition_j = (
    (abs($a - $c) == 2 && abs($b - $d) == 1) ||
    (abs($a - $c) == 1 && abs($b - $d) == 2)
);

echo "Ладья угрожает: " . ($condition_a ? "да" : "нет") . "<br>";
echo "Слон угрожает: " . ($condition_b ? "да" : "нет") . "<br>";
echo "Король может попасть за один ход: " . ($condition_c ? "да" : "нет") . "<br>";
echo "Ферзь угрожает: " . ($condition_g ? "да" : "нет") . "<br>";
echo "Белая пешка может попасть за один ход: " . ($condition_d ? "да" : "нет") . "<br>";
echo "Черная пешка может попасть за один ход: " . ($condition_e ? "да" : "нет") . "<br>";
echo "Конь угрожает: " . ($condition_j ? "да" : "нет") . "<br>";
?>