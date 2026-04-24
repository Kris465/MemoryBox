<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Конвертер чисел в текст</title>
</head>
<body>
    <h1>Конвертер чисел в текст</h1>
    <form method="post">
        <label for="number">Введите число (0-9999):</label>
        <input type="number" id="number" name="number" min="0" max="9999" required>
        <button type="submit">Конвертировать</button>
    </form>

    <?php
    function numberToWords($number) {
        $units = [
            0 => '',
            1 => 'один',
            2 => 'два',
            3 => 'три',
            4 => 'четыре',
            5 => 'пять',
            6 => 'шесть',
            7 => 'семь',
            8 => 'восемь',
            9 => 'девять',
        ];

        $teens = [
            10 => 'десять',
            11 => 'одиннадцать',
            12 => 'двенадцать',
            13 => 'тринадцать',
            14 => 'четырнадцать',
            15 => 'пятнадцать',
            16 => 'шестнадцать',
            17 => 'семнадцать',
            18 => 'восемнадцать',
            19 => 'девятнадцать',
        ];

        $tens = [
            2 => 'двадцать',
            3 => 'тридцать',
            4 => 'сорок',
            5 => 'пятьдесят',
            6 => 'шестьдесят',
            7 => 'семьдесят',
            8 => 'восемьдесят',
            9 => 'девяносто',
        ];

        $hundreds = [
            1 => 'сто',
            2 => 'двести',
            3 => 'триста',
            4 => 'четыреста',
            5 => 'пятьсот',
            6 => 'шестьсот',
            7 => 'семьсот',
            8 => 'восемьсот',
            9 => 'девятьсот',
        ];

        $thousands = [
            1 => 'тысяча',
            2 => 'две тысячи',
            3 => 'три тысячи',
            4 => 'четыре тысячи',
            5 => 'пять тысяч',
            6 => 'шесть тысяч',
            7 => 'семь тысяч',
            8 => 'восемь тысяч',
            9 => 'девять тысяч',
        ];

        if ($number == 0) {
            return 'ноль';
        }

        $words = '';

        // Обработка тысяч
        if ($number >= 1000) {
            $thousand = floor($number / 1000);
            $words .= $thousands[$thousand] . ' ';
            $number %= 1000;
        }

        // Обработка сотен
        if ($number >= 100) {
            $hundred = floor($number / 100);
            $words .= $hundreds[$hundred] . ' ';
            $number %= 100;
        }

        // Обработка десятков
        if ($number >= 20) {
            $ten = floor($number / 10);
            $words .= $tens[$ten] . ' ';
            $number %= 10;
        }

        // Обработка десятков от 10 до 19
        if ($number >= 10) {
            $words .= $teens[$number] . ' ';
            $number = 0;
        }

        // Обработка единиц
        if ($number > 0) {
            $words .= $units[$number] . ' ';
        }

        return trim($words);
    }

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $number = intval($_POST['number']);
        if ($number >= 0 && $number <= 9999) {
            echo "<h2>Результат: " . numberToWords($number) . "</h2>";
        } else {
            echo "<h2>Пожалуйста, введите число от 0 до 9999.</h2>";
        }
    }
    ?>
</body>
</html>