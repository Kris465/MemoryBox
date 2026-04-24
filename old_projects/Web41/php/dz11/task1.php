<?php

class StringUtils {
    
    public static function countCharacter($string, $char) {
        if (strlen($char) !== 1) {
            throw new InvalidArgumentException("Второй параметр должен быть одним символом.");
        }
        return substr_count($string, $char);
    }

    public static function replaceCharacter($string, $oldChar, $newChar) {
        if (strlen($oldChar) !== 1 || strlen($newChar) !== 1) {
            throw new InvalidArgumentException("Оба параметра должны быть одним символом.");
        }
        return str_replace($oldChar, $newChar, $string);
    }

    public static function reverseString($string) {
        return strrev($string);
    }

    public static function splitStringToWords($string) {
        return preg_split('/\s+/', trim($string));
    }

    public static function detectLanguage($string) {
        if (preg_match('/[а-яА-ЯЁё]/u', $string)) {
            return 'Cyrillic';
        } elseif (preg_match('/[a-zA-Z]/u', $string)) {
            return 'Latin';
        } else {
            return 'Unknown';
        }
    }
}

// Обработка формы
$result = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = $_POST['action'];
    $inputString = $_POST['inputString'];
    
    switch ($action) {
        case 'count':
            $char = $_POST['char'];
            $result = "Количество '{$char}' в '{$inputString}': " . StringUtils::countCharacter($inputString, $char);
            break;
        case 'replace':
            $oldChar = $_POST['oldChar'];
            $newChar = $_POST['newChar'];
            $result = "Замена '{$oldChar}' на '{$newChar}' в '{$inputString}': " . StringUtils::replaceCharacter($inputString, $oldChar, $newChar);
            break;
        case 'reverse':
            $result = "Строка '{$inputString}' задом наперед: " . StringUtils::reverseString($inputString);
            break;
        case 'split':
            $words = StringUtils::splitStringToWords($inputString);
            $result = "Разбиение строки '{$inputString}' на слова: " . implode(', ', $words);
            break;
        case 'detect':
            $result = "Язык слова '{$inputString}': " . StringUtils::detectLanguage($inputString);
            break;
        default:
            $result = "Неизвестное действие.";
    }
}
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>String Utils</title>
</head>
<body>
    <h1>Библиотека для работы со строками</h1>
    <form method="post">
        <label for="inputString">Введите строку:</label><br>
        <input type="text" id="inputString" name="inputString" required><br><br>

        <label for="action">Выберите действие:</label><br>
        <select id="action" name="action" required>
            <option value="count">Подсчитать символ</option>
            <option value="replace">Заменить символ</option>
            <option value="reverse">Вывести задом наперед</option>
            <option value="split">Разбить на слова</option>
            <option value="detect">Определить язык</option>
        </select><br><br>

        <div id="countOptions" style="display:none;">
            <label for="char">Символ для подсчета:</label><br>
            <input type="text" id="char" name="char" maxlength="1"><br><br>
        </div>

        <div id="replaceOptions" style="display:none;">
            <label for="oldChar">Символ для замены:</label><br>
            <input type="text" id="oldChar" name="oldChar" maxlength="1"><br><br>
            <label for="newChar">Новый символ:</label><br>
            <input type="text" id="newChar" name="newChar" maxlength="1"><br><br>
        </div>

        <button type="submit">Выполнить</button>
    </form>

    <div>
        <h2>Результат:</h2>
        <p><?php echo $result; ?></p>
    </div>

    <script>
        const actionSelect = document.getElementById('action');
        const countOptions = document.getElementById('countOptions');
        const replaceOptions = document.getElementById('replaceOptions');

        actionSelect.addEventListener('change', function() {
            countOptions.style.display = 'none';
            replaceOptions.style.display = 'none';

            if (this.value === 'count') {
                countOptions.style.display = 'block';
            } else if (this.value === 'replace') {
                replaceOptions.style.display = 'block';
            }
        });
    </script>
</body>
</html>