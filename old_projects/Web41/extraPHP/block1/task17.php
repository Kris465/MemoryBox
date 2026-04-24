<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        .result {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
<?php

function solve() {
    $vars = [
        'x' => 1, 'x1' => 2, 'x2' => 3, 'x3' => 4,
        'v0' => 5, 'a' => 6, 't' => 7, 'm' => 8,
        'v' => 9, 'g' => 10, 'h' => 11, 'R1' => 12,
        'R2' => 13, 'I' => 14, 'b' => 15, 'c' => 16,
        'd' => 17, 'R' => 18, 'r'=> 19
    ]; 

    $expressions = [
        'a' => fn($x) => ($x * $x - 1) / ($x * $x + 2),
        'b' => fn($x1, $x2, $x3) => ($x1 * $x2) + ($x1 * $x3) + ($x2 * $x3),
        'c' => fn($v0, $a, $t) => $v0 * $t + ($a * $t * $t) / 2,
        'd' => fn($m, $v, $g, $h) => ($m * $v * $v) / 2 - $m * $g * $h,
        'e' => fn($R1, $R2) => $R1 + $R2 / ($R1 * $R2),
        'f' => fn($m, $g) => cos($m * $g),
        'g' => fn($R) => 2 * $R,
        'h' => fn($b, $a, $c) => sqrt($b * $b - 4 * $a * $c),
        'i' => fn($m, $r) => ($m * $m) / ($r * $r), 
        'j' => fn($I, $R) => $I * $I * $R,
        'k' => fn($a, $b, $c) => sin($a * $b) / $c,
        'l' => fn($a, $b, $c) => sqrt($a * $a + $b * $b - 2 * $a * $b * cos($c)),
        'm' => fn($a, $d, $b, $c) => ($a * $d - $b * $c) / ($a * $d),
        'n' => fn($x) => 2 * sin($x) + 1,
        'o' => fn($a, $b, $c) => (-$b + sqrt($b * $b - 4 * $a * $c)) / (2 * $a),
        'p' => fn($x, $x1, $x2) => ($x - $x1) / ($x2 - $x1),
        'q' => fn($x) => 1 / ($x * $x),
        'r' => fn($x) => 1 / $x,
    ];

    echo "<h2>Результаты:</h2>";
    echo "<div>";
    foreach ($expressions as $key => $expression) {
        $params = [];
        $reflection = new ReflectionFunction($expression);
        foreach ($reflection->getParameters() as $param) {
            $name = $param->getName();
            $params[] = $vars[$name]; 
        }
        $result = $expression(...$params);
        echo "<div class='result'>" . str_pad($key . ":", 5) . $result . "</div>";
    }
    echo "</div>";
}

solve();
?>
</body>
</html>