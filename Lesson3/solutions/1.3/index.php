<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Калькулятор</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

<div class="container">
    <?php
    $result = '';
    
    // Проверяем, была ли форма отправлена
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $num1 = floatval($_POST['num1']);
        $num2 = floatval($_POST['num2']);
        $operation = $_POST['operation'];

        // Выполняем вычисления в зависимости от выбранного символа
        switch ($operation) {
            case '+':
                $result = $num1 + $num2;
                break;
            case '-':
                $result = $num1 - $num2;
                break;
            case '*':
                $result = $num1 * $num2;
                break;
            case '/':
                if ($num2 != 0) {
                    $result = $num1 / $num2;
                } else {
                    $result = 'Ошибка: деление на ноль!';
                }
                break;
            default:
                $result = 'Неизвестная операция';
        }
    }
    ?>

    <?php if ($result === ''): ?>
        <form method="post" action="">
            <input type="number" name="num1" placeholder="Первое число" required>
            <select name="operation" required>
                <option value="+">+</option>
                <option value="-">-</option>
                <option value="*">*</option>
                <option value="/">/</option>
            </select>
            <input type="number" name="num2" placeholder="Второе число" required>
            <input type="submit" value="Вычислить">
        </form>
    <?php endif; ?>

    <?php if ($result !== ''): ?>
        <p class="result">Результат: <?php echo $result; ?></p>
    <?php endif; ?>
</div>

</body>
</html>
