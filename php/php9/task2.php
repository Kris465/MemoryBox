<?php
/**
 * @param int
 * @return string 
 */
function numberToWords(int $number): string {
    if ($number === 0) {
        return 'ноль';
    }

    $result = [];
    $negative = false;

    if ($number < 0) {
        $negative = true;
        $number = abs($number);
    }

    $units = $number % 10;
    $tens = (int)($number / 10) % 10;
    $hundreds = (int)($number / 100) % 10;
    $thousands = (int)($number / 1000) % 1000;

    if ($thousands > 0) {
        $thousandWords = numberToWords($thousands);

        $lastTwo = $thousands % 100;
        $lastOne = $thousands % 10;
        
        if ($lastTwo >= 11 && $lastTwo <= 14) {
            $thousandWords .= ' тысяч';
        } else {
            switch ($lastOne) {
                case 1:
                    $thousandWords .= ' тысяча';
                    break;
                case 2:
                case 3:
                case 4:
                    $thousandWords .= ' тысячи';
                    break;
                default:
                    $thousandWords .= ' тысяч';
            }
        }
        
        $result[] = $thousandWords;
    }

    $hundredsWords = [
        1 => 'сто',
        2 => 'двести',
        3 => 'триста',
        4 => 'четыреста',
        5 => 'пятьсот',
        6 => 'шестьсот',
        7 => 'семьсот',
        8 => 'восемьсот',
        9 => 'девятьсот'
    ];
    
    if ($hundreds > 0) {
        $result[] = $hundredsWords[$hundreds];
    }

    $tensWords = [
        1 => [
            'десять',
            'одиннадцать',
            'двенадцать',
            'тринадцать',
            'четырнадцать',
            'пятнадцать',
            'шестнадцать',
            'семнадцать',
            'восемнадцать',
            'девятнадцать'
        ],
        2 => 'двадцать',
        3 => 'тридцать',
        4 => 'сорок',
        5 => 'пятьдесят',
        6 => 'шестьдесят',
        7 => 'семьдесят',
        8 => 'восемьдесят',
        9 => 'девяносто'
    ];
    
    $unitsWords = [
        1 => 'один',
        2 => 'два',
        3 => 'три',
        4 => 'четыре',
        5 => 'пять',
        6 => 'шесть',
        7 => 'семь',
        8 => 'восемь',
        9 => 'девять'
    ];
    if ($tens === 1) {
        $result[] = $tensWords[1][$units];
    } else {
        if ($tens > 1) {
            $result[] = $tensWords[$tens];
        }
        
        if ($units > 0) {
            $result[] = $unitsWords[$units];
        }
    }
    if ($negative) {
        array_unshift($result, 'минус');
    }
    return implode(' ', $result);
}

$number = null;
$result = '';
$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['number'])) {
    $input = trim($_POST['number']);
    
    if ($input === '') {
        $error = 'Пожалуйста, введите число';
    } elseif (!is_numeric($input)) {
        $error = 'Введите корректное число';
    } else {
        $number = (int)$input;

        if ($number < -999999 || $number > 999999) {
            $error = 'Число должно быть между -999999 и 999999';
        } else {
            $result = numberToWords($number);
        }
    }
}
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Конвертер чисел в слова</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
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
            margin-top: 0;
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
        .result {
            margin-top: 20px;
            padding: 15px;
            background-color: #e8f5e9;
            border-radius: 4px;
            border-left: 4px solid #4CAF50;
        }
        .error {
            margin-top: 20px;
            padding: 15px;
            background-color: #ffebee;
            border-radius: 4px;
            border-left: 4px solid #f44336;
        }
        .examples {
            margin-top: 20px;
            font-size: 14px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Конвертер чисел в слова</h1>
        <form method="POST">
            <div class="form-group">
                <label for="number">Введите число (от -999999 до 999999):</label>
                <input type="text" id="number" name="number" 
                       value="<?= isset($_POST['number']) ? htmlspecialchars($_POST['number']) : '' ?>"
                       placeholder="Например: 4532">
            </div>
            <button type="submit">Конвертировать</button>
        </form>
        <?php if ($error): ?>
            <div class="error">
                <strong>Ошибка:</strong> <?= htmlspecialchars($error) ?>
            </div>
        <?php elseif ($result !== ''): ?>
            <div class="result">
                <strong>Результат:</strong><br>
                <?= htmlspecialchars($number) ?> — <?= htmlspecialchars($result) ?>
            </div>
        <?php endif; ?>
    </div>
</body>
</html>