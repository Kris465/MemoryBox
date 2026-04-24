<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<title>Проверка одинакового роста</title>
</head>
<body>
<h2>Проверка, одинаков ли рост трех человек</h2>
<form method="post">
Рост 1: <input type="number" step="any" name="height1" required><br><br>
Рост 2: <input type="number" step="any" name="height2" required><br><br>
Рост 3: <input type="number" step="any" name="height3" required><br><br>
<input type="submit" value="Проверить">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$h1 = floatval($_POST['height1']);
$h2 = floatval($_POST['height2']);
$h3 = floatval($_POST['height3']);

if ($h1 == $h2 && $h2 == $h3) {
    echo "<p>Все три человека имеют одинаковый рост.</p>";
} else {
    echo "<p>Рост у людей не одинаковый.</p>";
}
}
?>
</body>
</html>