<?php
function checkConditions($x, $y) {
    $a = ($x > 2) && ($y > 3);
    
    $b = ($x > 1) || ($y > 2);
    
    $v = ($x < 0) || ($y < 5);
    
    $g = ($x > 3) || ($y > 1);
    
    $d = ($x > 3) && ($x < 10);
    
    $e = !($x > 2);
    
    $zh = !(($x > 0) && ($x < 5));
    
    $z = ($x > 10) && ($x < 20);
    
    $i = ($y > 0) && ($y < 4) && ($x < 5);
    
    return [
        'а) x > 2 и y > 3' => $a,
        'б) x > 1 или y > 2' => $b,
        'в) x < 0 или y < 5' => $v,
        'г) x > 3 или y > 1' => $g,
        'д) x > 3 и x < 10' => $d,
        'е) неверно, что x > 2' => $e,
        'ж) неверно, что x > 0 и x < 5' => $zh,
        'з) 10 < x < 20' => $z,
        'и) 0 < y < 4 и x < 5' => $i
    ];
}

$x = 4;
$y = 3;
$results = checkConditions($x, $y);

echo "Для x = $x, y = $y:\n";
foreach ($results as $condition => $result) {
    echo $condition . ": " . ($result ? 'Истина' : 'Ложь') . "\n";
}
?>