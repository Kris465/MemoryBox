<?php
/**
 * @param array
 * @return bool
 */
function highlightNegativeNumbers(array $numbers): bool {
    if (empty($numbers)) {
        echo "<p>Передан пустой массив</p>";
        return false;
    }
    foreach ($numbers as $number) {
        if (!is_numeric($number)) {
            echo "<p>Массив должен содержать только числа! Найдено нечисловое значение: " . htmlspecialchars($number) . "</p>";
            return false;
        }
    }
    echo '<div style="font-family: Arial, sans-serif; margin: 20px;">';
    echo '<h3>Результат обработки массива:</h3>';
    echo '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 20px;">';

    foreach ($numbers as $number) {
        if ($number < 0) {
            echo '<span style="color: red; font-weight: bold; padding: 5px; border: 1px solid #ddd; border-radius: 3px;">' . htmlspecialchars($number) . '</span>';
        } else {
            echo '<span style="padding: 5px; border: 1px solid #ddd; border-radius: 3px;">' . htmlspecialchars($number) . '</span>';
        }
    }
    echo '</div>';
    echo '<p>Отрицательные числа выделены <span style="color: red; font-weight: bold;">красным цветом</span></p>';
    echo '</div>';
    return true;
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $input = $_POST['numbers'] ?? '';

    $numbers = explode(',', $input);

    $numbers = array_map('trim', $numbers);
    $numbers = array_filter($numbers, function($item) {
        return $item !== '';
    });
    
    $numbers = array_map(function($item) {
        return is_numeric($item) ? $item + 0 : $item;
    }, $numbers);
}
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Выделение отрицательных чисел</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }
        .container {
            background-color: #f9f9f9;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
            font-size: 16px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 15px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 4px;
            width: 100%;
        }
        button:hover {
            background-color: #45a049;
        }
        .example {
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 4px;
            margin-top: 15px;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Выделение отрицательных чисел в массиве</h1>
        <form method="POST">
            <div class="form-group">
                <label for="numbers">Введите числа через запятую:</label>
                <input type="text" id="numbers" name="numbers" required
                       placeholder="Например: 5, -2, 10, -3, 0, 7.5, -1">
            </div>
            <button type="submit">Обработать массив</button>
        </form>
        <?php
        if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($numbers)) {
            echo '<div style="margin-top: 30px;">';
            $result = highlightNegativeNumbers($numbers);
            echo '<p>Статус выполнения: ' . ($result ? 'Успешно' : 'Ошибка') . '</p>';
            echo '</div>';
        }
        ?>
    </div>
</body>
</html>