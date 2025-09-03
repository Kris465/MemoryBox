<?php
function createHtmlElement($tag, $class = '', $content = '', $selfClosing = false) {
    if (!preg_match('/^[a-z][a-z0-9]*$/i', $tag)) {
        return 'Неверное имя тега!';
    }

    $content = htmlspecialchars($content, ENT_QUOTES, 'UTF-8');
    $class = htmlspecialchars(trim($class), ENT_QUOTES, 'UTF-8');

    $classAttr = $class !== '' ? ' class="' . $class . '"' : '';

    if ($selfClosing) {
        return "<{$tag}{$classAttr} />";
    } else {
        return "<{$tag}{$classAttr}>{$content}</{$tag}>";
    }
}

$htmlOutput = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $tag = $_POST['tag'] ?? '';
    $class = $_POST['class'] ?? '';
    $content = $_POST['content'] ?? '';

    $selfClosingTags = ['img', 'br', 'hr', 'input', 'meta', 'link'];
    $selfClosing = in_array(strtolower($tag), $selfClosingTags);
    
    $htmlOutput = createHtmlElement($tag, $class, $content, $selfClosing);
}
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Генератор HTML-элементов</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input[type="text"], textarea { width: 100%; padding: 8px; box-sizing: border-box; }
        button { background: #4CAF50; color: white; border: none; padding: 10px 15px; cursor: pointer; }
        button:hover { background: #45a049; }
        .output { margin-top: 20px; padding: 15px; background: #f5f5f5; border: 1px solid #ddd; }
        .output pre { margin: 0; white-space: pre-wrap; }
    </style>
</head>
<body>
    <h1>Генератор HTML-элементов</h1>
    <form method="POST">
        <div class="form-group">
            <label for="tag">Название тега:</label>
            <input type="text" id="tag" name="tag" required placeholder="Например: div, p, span">
        </div>
        
        <div class="form-group">
            <label for="class">Класс стилей:</label>
            <input type="text" id="class" name="class" placeholder="Например: container highlight">
        </div>
        
        <div class="form-group">
            <label for="content">Содержимое (если нужно):</label>
            <textarea id="content" name="content" rows="3"></textarea>
        </div>
        <button type="submit">Создать элемент</button>
    </form>
    <?php if ($htmlOutput): ?>
    <div class="output">
        <h3>Результат:</h3>
        <p>HTML-код:</p>
        <pre><?= htmlspecialchars($htmlOutput) ?></pre>
        
        <p>Отображение:</p>
        <?= $htmlOutput ?>
    </div>
    <?php endif; ?>
</body>
</html>