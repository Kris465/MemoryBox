<?php
if (!isset($_GET['a']) || !isset($_GET['b']) || !isset($_GET['c']) || !isset($_GET['d']) || !isset($_GET['e'])) {
    echo "Пожалуйста, передайте размеры стола (a, b) и костей (c, d, e) через параметры URL.";
    exit;
}

$a = intval($_GET['a']);
$b = intval($_GET['b']);
$c = intval($_GET['c']);
$d = intval($_GET['d']);
$e = intval($_GET['e']);

$max_count = 0;

$orientations = [
    [$c, $d],
    [$d, $c],
];

foreach ($orientations as $size) {
    list($w, $h) = $size;


    if ($w <= $a && $h <= $b) {
        $count_along_width = floor($a / $w) * floor($b / $h);
        if ($count_along_width > $max_count) {
            $max_count = $count_along_width;
        }
    }

    if ($h <= $a && $w <= $b) {
        $count_along_height = floor($a / $h) * floor($b / $w);
        if ($count_along_height > $max_count) {
            $max_count = $count_along_height;
        }
    }
}

echo "Максимальное количество костей: " . $max_count;
?>