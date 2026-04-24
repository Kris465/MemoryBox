<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<title>Проверка возможности размещения коробки в чемодане</title>
</head>
<body>
<h2>Можно ли разместить коробку внутри чемодана с учетом параллельности или перпендикулярности сторон</h2>
<form method="post">
a1 (размер чемодана): <input type="number" step="any" name="a1" required><br><br>
a2 (размер чемодана): <input type="number" step="any" name="a2" required><br><br>
a3 (размер чемодана): <input type="number" step="any" name="a3" required><br><br>
b1 (размер коробки): <input type="number" step="any" name="b1" required><br><br>
b2 (размер коробки): <input type="number" step="any" name="b2" required><br><br>
b3 (размер коробки): <input type="number" step="any" name="b3" required><br><br>
<input type="submit" value="Проверить">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$a = [
    floatval($_POST['a1']),
    floatval($_POST['a2']),
    floatval($_POST['a3'])
];

$b = [
    floatval($_POST['b1']),
    floatval($_POST['b2']),
    floatval($_POST['b3'])
];


$permutationsA = permute($a);
$permutationsB = permute($b);

$can_fit = false;

foreach ($permutationsA as $dimsA) {
    foreach ($permutationsB as $dimsB) {
  
        if (
            $dimsB[0] <= $dimsA[0] &&
            $dimsB[1] <= $dimsA[1] &&
            $dimsB[2] <= $dimsA[2]
        ) {
            $can_fit = true;
            break 2; 
        }
    }
}


function permute(array $items) {
    if (count($items) <= 1) {
        return [$items];
    }
    $result = [];
    for ($i = 0; $i < count($items); $i++) {
        $first = $items[$i];
        $remaining = array_diff_key($items, [$i => $first]);
        foreach (permute(array_values($remaining)) as $perm) {
            array_unshift($perm, $first);
            $result[] = $perm;
        }
    }
    return $result;
}

if ($can_fit) {
    echo "<p>Коробка может быть размещена внутри чемодана.</p>";
} else {
    echo "<p>Коробка не может быть размещена внутри чемодана.</p>";
}
}
?>
</body>
</html>