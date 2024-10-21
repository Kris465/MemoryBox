<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Перевод в римские цифры</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Перевод числа в римские цифры</h1>
        <form method="POST" action="">
            <label for="number">Введите число (1-3999):</label>
            <input type="number" id="number" name="number" min="1" max="3999" required>
            <input type="submit" value="Перевести">
        </form>

        <?php
        function toRoman($num) {
            $map = [
                4000 => 'MMMM',
                3000 => 'MMM',
                2000 => 'MM',
                1000 => 'M',
                900 => 'CM',
                500 => 'D',
                400 => 'CD',
                300 => 'CCC',
                200 => 'CC',
                100 => 'C',
                90 => 'XC',
                50 => 'L',
                40 => 'XL',
                30 => 'XXX',
                20 => 'XX',
                10 => 'X',
                9 => 'IX',
                5 => 'V',
                4 => 'IV',
                3 => 'III',
                2 => 'II',
                1 => 'I'
            ];

            $result = '';
            foreach ($map as $value => $symbol) {
                while ($num >= $value) {
                    $result .= $symbol;
                    $num -= $value;
                }
            }
            return $result;
        }

        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $number = (int)$_POST['number'];
            if ($number < 1 || $number > 3999) {
                echo "<p class='error'>Пожалуйста, введите число от 1 до 3999.</p>";
            } else {
                $roman = toRoman($number);
                echo "<h2>Результат:</h2>";
                echo "<p>Римские цифры: <strong>$roman</strong></p>";
            }
        }
        ?>
    </div>
</body>
</html>
