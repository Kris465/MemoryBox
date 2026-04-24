

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Калькулятор с скобками</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        input { padding: 8px; font-size: 16px; }
        button { padding: 8px 15px; font-size: 16px; }
    </style>
</head>
<body>
    <h1>Калькулятор (скобки + многозначные числа)</h1>
    <form method="POST">
        <label for="expression">Введите выражение:</label><br>
        <input type="text" id="expression" name="expression" placeholder="Пример: (10+2)*3" required>
        <button type="submit">Вычислить</button>
    </form>
</body>
</html>

<?php
function calculateExpression(string $expression): float {
    $expression = str_replace(' ', '', $expression);
    if (substr_count($expression, '(') !== substr_count($expression, ')')) {
        throw new Exception("Непарные скобки!");
    }

    while (($openPos = strrpos($expression, '(')) !== false) {
        $closePos = strpos($expression, ')', $openPos);
        if ($closePos === false) {
            throw new Exception("Непарные скобки!");
        }

        $subExpr = substr($expression, $openPos + 1, $closePos - $openPos - 1);
        $subResult = calculateSubExpression($subExpr);
        $expression = substr_replace($expression, $subResult, $openPos, $closePos - $openPos + 1);
    }

    return calculateSubExpression($expression);
}

function calculateSubExpression(string $expression): float {
    preg_match_all('/(\d+\.?\d*|[+\-*\/])/', $expression, $matches);
    $tokens = $matches[0];

    for ($i = 1; $i < count($tokens); $i += 2) {
        $operator = $tokens[$i];
        if ($operator === '*' || $operator === '/') {
            $left = (float)$tokens[$i - 1];
            $right = (float)$tokens[$i + 1];
            $result = $operator === '*' ? $left * $right : $left / $right;
            array_splice($tokens, $i - 1, 3, $result);
            $i -= 2;
        }
    }

    $result = (float)$tokens[0];
    for ($i = 1; $i < count($tokens); $i += 2) {
        $operator = $tokens[$i];
        $number = (float)$tokens[$i + 1];
        $result = $operator === '+' ? $result + $number : $result - $number;
    }

    return $result;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['expression'])) {
    $expression = $_POST['expression'];
    try {
        $result = calculateExpression($expression);
        echo "<p>Результат: <strong>" . htmlspecialchars($result) . "</strong></p>";
    } catch (Exception $e) {
        echo "<p style='color: red;'>Ошибка: " . htmlspecialchars($e->getMessage()) . "</p>";
    }
}
?>