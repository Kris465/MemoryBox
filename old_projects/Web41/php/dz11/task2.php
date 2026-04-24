<?php
class StringManipulator {

    public function find($string, $substring) {
        $position = strpos($string, $substring);
        return $position !== false ? $position : "Подстрока не найдена.";
    }

    public function replace($string, $search, $replace) {
        return str_replace($search, $replace, $string);
    }

    public function reflect($string) {
        return strrev($string);
    }

    public function split($string, $delimiter) {
        return explode($delimiter, $string);
    }

    public function uniqueLetters($string) {
        return implode(", ", array_unique(str_split($string)));
    }
}

$stringManipulator = new StringManipulator();

$findResult = '';
$replaceResult = '';
$reflectResult = '';
$splitResult = [];
$uniqueLettersResult = '';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $inputString = $_POST['inputString'];
    $substring = $_POST['substring'];
    $search = $_POST['search'];
    $replace = $_POST['replace'];
    $delimiter = $_POST['delimiter'];

    $findResult = $stringManipulator->find($inputString, $substring);
    $replaceResult = $stringManipulator->replace($inputString, $search, $replace);
    $reflectResult = $stringManipulator->reflect($inputString);
    $splitResult = $stringManipulator->split($inputString, $delimiter);
    $uniqueLettersResult = $stringManipulator->uniqueLetters($inputString);
}
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Строковые функции</title>
</head>
<body>
    <h1>Строковые функции</h1>
    <form method="post">
        <label for="inputString">Введите строку:</label><br>
        <input type="text" id="inputString" name="inputString" required><br><br>

        <label for="substring">Подстрока для поиска:</label><br>
        <input type="text" id="substring" name="substring" required><br><br>

        <label for="search">Подстрока для замены:</label><br>
        <input type="text" id="search" name="search" required><br><br>

        <label for="replace">На что заменить:</label><br>
        <input type="text" id="replace" name="replace" required><br><br>

        <label for="delimiter">Разделитель для разделения строки:</label><br>
        <input type="text" id="delimiter" name="delimiter" required><br><br>

        <input type="submit" value="Выполнить">
    </form>

    <?php if ($_SERVER["REQUEST_METHOD"] == "POST"): ?>
        <h2>Результаты:</h2>
        <p><strong>Исходная строка:</strong> <?php echo htmlspecialchars($inputString); ?></p>
        <p><strong>Результат find:</strong> <?php echo $findResult; ?></p>
        <p><strong>Результат replace:</strong> <?php echo $replaceResult; ?></p>
        <p><strong>Результат reflect:</strong> <?php echo $reflectResult; ?></p>
        <p><strong>Результат split:</strong> <?php echo implode(", ", $splitResult); ?></p>
        <p><strong>Уникальные буквы:</strong> <?php echo $uniqueLettersResult; ?></p>
    <?php endif; ?>
</body>
</html>