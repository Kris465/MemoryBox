<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<title>Проверка прохождения кирпича через отверстие</title>
</head>
<body>
<h2>Можно ли вставить кирпич с ребрами a, b, c в отверстие со сторонами x и y</h2>
<form method="post">
a (ребро кирпича): <input type="number" step="any" name="a" required><br><br>
b (ребро кирпича): <input type="number" step="any" name="b" required><br><br>
c (ребро кирпича): <input type="number" step="any" name="c" required><br><br>
x (сторона отверстия): <input type="number" step="any" name="x" required><br><br>
y (сторона отверстия): <input type="number" step="any" name="y" required><br><br>
<input type="submit" value="Проверить">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$a = floatval($_POST['a']);
$b = floatval($_POST['b']);
$c = floatval($_POST['c']);
$x = floatval($_POST['x']);
$y = floatval($_POST['y']);


$possible_orientations = [
    [$a, $b],
    [$a, $c],
    [$b, $c]
];

$can_pass = false;

foreach ($possible_orientations as $dims) {
    sort($dims);
    $side1 = $dims[0];
    $side2 = $dims[1];


    if (($side1 <= $x && $side2 <= $y) || ($side1 <= $y && $side2 <= $x)) {
        $can_pass = true;
        break;
    }
}

if ($can_pass) {
    echo "<p>Кирпич пройдет через отверстие.</p>";
} else {
    echo "<p>Кирпич не пройдет через отверстие.</p>";
}
}
?>
</body>
</html>