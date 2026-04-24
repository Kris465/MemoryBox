<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php

function solve() {
    $a = 1; $b = 2; $c = 3; $x = 4; $R = 5; 

    $expressions = [
        'a' => fn($a, $b, $c) => $a / ($b / $c),
        'b' => fn($a, $b, $c) => $a * $b * $c,
        'c' => fn($a, $b, $c) => ($a / $b) * $c, 
        'd' => fn($a, $b, $c) => $a / ($b * $c),
        'e' => fn($a, $b, $c) => $a / ($b * $b * $c),
        'f' => fn($a, $b, $c) => $a / $b / ($b * $c),
        'g' => fn($a, $b) => sin($a / $b),
        'h' => fn($a, $b, $x) => (12 * sin($a * $b)) / $x,
        'i' => fn($b, $c, $a) => (2 * cos(2 * $b * $c)) / ($a * $b * $c),
        'j' => fn($R, $a, $b, $c) => (4 * sin(2 * sin(2 * sin(2 * $R)))) / ($a * $b * $c),
        'k' => fn($a, $x, $b, $c, $d) => ($a / $x + $b) / ($c * $x + $d),
        'l' => fn($a, $b) => (2 * sin(2) / cos(2)) * ($a / $b) / ($a / $b),
        'm' => fn($x) => abs(2 * sin(3 * abs(2) / $x)),
    ];

    $argsMap = [ 
        'a' => [$a, $b, $c], 'b' => [$a, $b, $c], 'c' => [$a, $b, $c],
        'd' => [$a, $b, $c], 'e' => [$a, $b, $c], 'f' => [$a, $b, $c],
        'g' => [$a, $b],       'h' => [$a, $b, $x],   'i' => [$b, $c, $a],
        'j' => [$R, $a, $b, $c], 'k' => [$a, $x, $b, $c, $R],
        'l' => [$a, $b], 'm' => [$x]
    ];

    foreach ($expressions as $key => $expression) {
        echo "$key: " . $expression(...$argsMap[$key]) . "\n";
    }
}

solve();

?>
</body>
</html>