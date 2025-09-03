<!DOCTYPE html>
<html>
<head>
    <title>Тестирование StringUtils</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .test-case { margin-bottom: 20px; padding: 10px; border: 1px solid #ddd; }
        .success { background-color: #e6ffe6; }
        .error { background-color: #ffe6e6; }
    </style>
</head>
<body>
<h1>Тестирование библиотеки StringUtils</h1>

<?php
require_once 'StringUtils.php';

function runTest($description, $expected, $actual) {
    $isSuccess = $expected === $actual;
    $class = $isSuccess ? 'success' : 'error';
    echo "<div class='test-case $class'>";
    echo "<h3>$description</h3>";
    echo "<p>Ожидаемый результат: <strong>" . htmlspecialchars(print_r($expected, true)) . "</strong></p>";
    echo "<p>Фактический результат: <strong>" . htmlspecialchars(print_r($actual, true)) . "</strong></p>";
    echo "</div>";
}

runTest(
    "a. Подсчет символа 'l' в строке 'hello world'",
    3,
    StringUtils::countChar("hello world", "l")
);

runTest(
    "b. Замена 'o' на '0' в строке 'hello world'",
    "hell0 w0rld",
    StringUtils::replaceChar("hello world", "o", "0")
);

runTest(
    "c. Реверс строки 'hello'",
    "olleh",
    StringUtils::reverse("hello")
);

runTest(
    "d. Разбиение строки 'hello world from php'",
    ["hello", "world", "from", "php"],
    StringUtils::splitToWords("hello world from php")
);

try {
    runTest(
        "e. Определение алфавита для 'привет'",
        "Cyrillic",
        StringUtils::detectAlphabet("привет")
    );
    
    runTest(
        "e. Определение алфавита для 'hello'",
        "Latin",
        StringUtils::detectAlphabet("hello")
    );
    
    try {
        StringUtils::detectAlphabet("приветhello");
        echo "<div class='test-case error'><h3>e. Тест на смешанный алфавит</h3><p>Ожидалось исключение, но его не было</p></div>";
    } catch (Exception $e) {
        echo "<div class='test-case success'><h3>e. Тест на смешанный алфавит</h3><p>Ожидаемое исключение получено: " . htmlspecialchars($e->getMessage()) . "</p></div>";
    }
} catch (Exception $e) {
    echo "<div class='test-case error'><h3>Ошибка при тестировании detectAlphabet</h3><p>" . htmlspecialchars($e->getMessage()) . "</p></div>";
}
?>
</body>
</html>