<?php

function strToBool($input) {
    if (is_bool($input)) return $input;
    $input = strtolower(trim($input));
    return in_array($input, ['true', '1', 'да', 'yes', 'y', 'on']);
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $X = isset($_POST['x']) ? strToBool($_POST['x']) : false;
    $Y = isset($_POST['y']) ? strToBool($_POST['y']) : false;
    $Z = isset($_POST['z']) ? strToBool($_POST['z']) : false;

    
    $result_a = (int)($X && !($Z || $Y) || !$Z);
    $result_b = (int)(!$X || $X && ($Y || $Z));
    $result_v = (int)(($X || $Y && !$Z) && $Z);
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Калькулятор логических выражений</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 20px auto; padding: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: inline-block; width: 120px; }
        select, button { padding: 8px; font-size: 16px; }
        button { background: #4CAF50; color: white; border: none; cursor: pointer; }
        .results { margin-top: 20px; padding: 15px; background: #f5f5f5; border-radius: 5px; }
        h2 { color: #333; }
    </style>
</head>
<body>
    <h2>Введите логические значения</h2>
    <form method="post">
        <div class="form-group">
            <label for="x">Значение X:</label>
            <select id="x" name="x">
                <option value="false">Ложь (false)</option>
                <option value="true">Истина (true)</option>
            </select>
        </div>
        
        <div class="form-group">
            <label for="y">Значение Y:</label>
            <select id="y" name="y">
                <option value="true">Истина (true)</option>
                <option value="false">Ложь (false)</option>
            </select>
        </div>
        
        <div class="form-group">
            <label for="z">Значение Z:</label>
            <select id="z" name="z">
                <option value="false">Ложь (false)</option>
                <option value="true">Истина (true)</option>
            </select>
        </div>
        
        <button type="submit">Вычислить</button>
    </form>

    <?php if ($_SERVER['REQUEST_METHOD'] === 'POST'): ?>
    <div class="results">
        <h3>Результаты для X=<?= $X ? 'true' : 'false' ?>, Y=<?= $Y ? 'true' : 'false' ?>, Z=<?= $Z ? 'true' : 'false' ?>:</h3>
        <p>а) X и не (Z или Y) или не Z: <strong><?= $result_a ?></strong></p>
        <p>б) не X или X и (Y или Z): <strong><?= $result_b ?></strong></p>
        <p>в) (X или Y и не Z) и Z: <strong><?= $result_v ?></strong></p>
        
        <h4>Пояснение:</h4>
        <ul>
            <li><strong>1</strong> означает "Истина" (true)</li>
            <li><strong>0</strong> означает "Ложь" (false)</li>
        </ul>
    </div>
    <?php endif; ?>
</body>
</html> 