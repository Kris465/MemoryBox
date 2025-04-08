<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Форма ввода</title>
</head>
<body>
    <h1>Проверка ввода</h1>
    <form action="" method="post">
        <label for="digits">Только цифры:</label>
        <input type="text" id="digits" name="digits" required><br><br>

        <label for="letters">Только буквы:</label>
        <input type="text" id="letters" name="letters" required><br><br>

        <label for="uppercase">Только заглавные буквы:</label>
        <input type="text" id="uppercase" name="uppercase" required><br><br>

        <input type="submit" value="Отправить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $pattern_digits = '/^d+$/';
        $pattern_letters = '/^[a-zA-Z]+$/';
        $pattern_uppercase = '/^[A-Z]+$/';
        $input_digits = $_POST['digits'];
        $input_letters = $_POST['letters'];
        $input_uppercase = $_POST['uppercase'];

        function validateInput($input, $pattern) {
            return preg_match($pattern, $input) === 1;
        }

        if (validateInput($input_digits, $pattern_digits)) {
            echo "<p>Ввод '$input_digits' содержит только цифры.</p>";
        } else {
            echo "<p style='color:red;'>Ошибка: ввод '$input_digits' содержит недопустимые символы (не только цифры).</p>";
        }

        if (validateInput($input_letters, $pattern_letters)) {
            echo "<p>Ввод '$input_letters' содержит только буквы.</p>";
        } else {
            echo "<p style='color:red;'>Ошибка: ввод '$input_letters' содержит недопустимые символы (не только буквы).</p>";
        }

        if (validateInput($input_uppercase, $pattern_uppercase)) {
            echo "<p>Ввод '$input_uppercase' содержит только заглавные буквы.</p>";
        } else {
            echo "<p style='color:red;'>Ошибка: ввод '$input_uppercase' содержит недопустимые символы (не только заглавные буквы).</p>";
        }
    }
    ?>
</body>
</html>
