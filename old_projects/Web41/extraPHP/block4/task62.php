<?php
$n = intval(trim(fgets(STDIN)));

$s = str_pad($n, 4, '0', STR_PAD_LEFT);

$digit_counts = array_count_values(str_split($s));

$has_three = false;
foreach ($digit_counts as $count) {
    if ($count == 3) {
        $has_three = true;
        break;
    }
}

if ($has_three) {
    echo "Да\n";
} else {
    echo "Нет\n";
}
?>