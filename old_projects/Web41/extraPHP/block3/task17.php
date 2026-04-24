<?php

function toBool($value) {
    $value = strtolower(trim($value));
    return in_array($value, ['1', 'true', 'yes', 'y', 'on']);
}

$result = null;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $A = isset($_POST['A']) ? toBool($_POST['A']) : false;
    $B = isset($_POST['B']) ? toBool($_POST['B']) : false;


    $expr_a = (!$A && !$B) || $A;

   
    $expr_b = $B || (!$A && !$B);

   
    $expr_c = $B && !($A && !$B);

    $result = [
        'expr_a' => $expr_a,
        'expr_b' => $expr_b,
        'expr_c' => $expr_c,
        'A' => $A,
        'B' => $B,
    ];
}
?>

<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<title>Вычисление логических выражений</title>
</head>
<body>

<h2>Введите значения логических величин A и B</h2>
<form method="post">
    <label for="A">A (true/false): </label>
    <input type="text" id="A" name="A" required><br><br>

    <label for="B">B (true/false): </label>
    <input type="text" id="B" name="B" required><br><br>

    <button type="submit">Вычислить</button>
</form>

<?php if ($result !== null): ?>
    <h3>Результаты вычислений:</h3>
    <p>A = <strong><?= $result['A'] ? 'true' : 'false' ?></strong></p>
    <p>B = <strong><?= $result['B'] ? 'true' : 'false' ?></strong></p>

    <ul>
        <li>а) !A && !B || A = <strong><?= $result['expr_a'] ? 'true' : 'false' ?></strong></li>
        <li>б) B || !A && !B = <strong><?= $result['expr_b'] ? 'true' : 'false' ?></strong></li>
        <li>в) B && !(A && !B) = <strong><?= $result['expr_c'] ? 'true' : 'false' ?></strong></li>
    </ul>
<?php endif; ?>

</body>
</html>