<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Выбор HTML-тега</title>
</head>
<body>

<h1>Выберите HTML-тег</h1>
<form method="post">
    <label for="tag">Выберите тег:</label>
    <select name="tag" id="tag" required>
        <option value="div">div</option>
        <option value="span">span</option>
        <option value="p">p</option>
        <option value="h1">h1</option>
        <option value="h2">h2</option>
        <option value="h3">h3</option>
        <option value="h4">h4</option>
        <option value="h5">h5</option>
        <option value="h6">h6</option>
        <option value="ul">ul</option>
        <option value="li">li</option>
        <option value="table">table</option>
        <option value="tr">tr</option>
        <option value="td">td</option>
        <option value="th">th</option>
        <option value="a">a</option>
        <option value="img">img</option>
    </select><br><br>

    <label for="styles">Введите стили (например, color: red;):</label>
    <input type="text" name="styles" id="styles" required><br><br>

    <label for="content">Введите содержимое:</label>
    <textarea name="content" id="content" rows="4" cols="50"></textarea><br><br>

    <input type="submit" value="Создать элемент">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $tag = $_POST['tag'];
    $styles = $_POST['styles'];
    $content = $_POST['content'];

    function createHtmlElement($tag, $styles, $content = '') {
        $validTags = ['div', 'span', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'li', 'table', 'tr', 'td', 'th', 'a', 'img'];
        
        if (in_array($tag, $validTags)) {
            return "<$tag style=\"$styles\">$content</$tag>";
        } else {
            return "Ошибка: недопустимый тег '$tag'.";
        }
    }

    $htmlElement = createHtmlElement($tag, $styles, $content);

    echo "<h2>Созданный HTML-элемент:</h2>";
    echo $htmlElement;
}
?>

</body>
</html>