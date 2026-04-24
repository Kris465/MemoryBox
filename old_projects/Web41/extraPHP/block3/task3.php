<?php

function strToBool($input) {
    if (is_bool($input)) return $input;
    $input = strtolower(trim($input));
    return in_array($input, ['true', '1', 'да', 'yes', 'y', 'on']);
}


if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $A = isset($_POST['a']) ? strToBool($_POST['a']) : false;
    $B = isset($_POST['b']) ? strToBool($_POST['b']) : false;
    $C = isset($_POST['c']) ? strToBool($_POST['c']) : false;
    

    $result_a = (int)(!$A && $B);
    $result_b = (int)($A || !$B);
    $result_c = (int)(($A && $B) || $C);
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Калькулятор логических выражений</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 500px; margin: 0 auto; padding: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: inline-block; width: 100px; }
        button { padding: 8px 15px; background: #4CAF50; color: white; border: none; cursor: pointer; }
        .results { margin-top: 20px; padding: 15px; background: #f5f5f5; }
    </style>
</head>
<body>
    <h2>Введите логические значения</h2>
    <form method="post">
        <div class="form-group">
            <label for="a">Значение A:</label>
            <select id="a" name="a">
                <option value="true">Истина (true)</option>
                <option value="false">Ложь (false)</option>
            </select>
        </div>
        
        <div class="form-group">
            <label for="b">Значение B:</label>
            <select id="b" name="b">
                <option value="true">Истина (true)</option>
                <option value="false" selected>Ложь (false)</option>
            </select>
        </div>
        
        <div class="form-group">
            <label for="c">Значение C:</label>
            <select id="c" name="c">
                <option value="true">Истина (true)</option>
                <option value="false" selected>Ложь (false)</option>
            </select>
        </div>
        
        <button type="submit">Вычислить</button>
    </form>

    <?php if ($_SERVER['REQUEST_METHOD'] === 'POST'): ?>
    <div class="results">
        <h3>Результаты:</h3>
        <p>а) не А и В: <?= $result_a ?></p>
        <p>б) А или не В: <?= $result_b ?></p>
        <p>в) А и В или С: <?= $result_c ?></p>
    </div>
    <?php endif; ?>
</body>
</html>