<?php
require_once 'Input.php';
require_once 'Radio.php';
require_once 'Checkbox.php';
require_once 'Select.php';
require_once 'Control.php';

function convertToHTML($object) {
    if ($object instanceof Radio) {
        return sprintf(
            '<input type="radio" name="%s" value="%s" style="background: %s; width: %spx; height: %spx;" %s>',
            htmlspecialchars($object->getName()),
            htmlspecialchars($object->getValue()),
            htmlspecialchars($object->getBackground()),
            htmlspecialchars($object->getWidth()),
            htmlspecialchars($object->getHeight()),
            $object->getCheckedState() ? 'checked' : ''
        );
    } elseif ($object instanceof Checkbox) {
        return sprintf(
            '<input type="checkbox" name="%s" value="%s" style="background: %s; width: %spx; height: %spx;" %s>',
            htmlspecialchars($object->getName()),
            htmlspecialchars($object->getValue()),
            htmlspecialchars($object->getBackground()),
            htmlspecialchars($object->getWidth()),
            htmlspecialchars($object->getHeight()),
            $object->getCheckedState() ? 'checked' : ''
        );
    } elseif ($object instanceof Select) {
        $options = '';
        foreach ($object->getItems() as $value => $label) {
            $options .= sprintf(
                '<option value="%s"%s>%s</option>',
                htmlspecialchars($value),
                $object->getValue() == $value ? ' selected' : '',
                htmlspecialchars($label)
            );
        }
        return sprintf(
            '<select name="%s" style="background: %s; width: %spx; height: %spx;">%s</select>',
            htmlspecialchars($object->getName()),
            htmlspecialchars($object->getBackground()),
            htmlspecialchars($object->getWidth()),
            htmlspecialchars($object->getHeight()),
            $options
        );
    } else {
        return '<!-- Unsupported object type -->';
    }
}

$username = new Input("#ffffff", 200, 30, "username", "");
$password = new Input("#ffffff", 200, 30, "password", "");
$gender = new Radio("#f0f0f0", 20, 20, "gender", "male", true);
$country = new Select("#e0e0e0", 200, 30, "country", "ru", [
    "ru" => "Россия",
    "us" => "США",
    "de" => "Германия"
]);
$subscribe = new Checkbox("#ffffff", 20, 20, "subscribe", "yes", true);

?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Форма регистрации</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: inline-block; width: 150px; }
    </style>
</head>
<body>
    <h1>Регистрация</h1>
    <form action="/submit" method="post">
        <div class="form-group">
            <label for="username">Имя пользователя:</label>
            <?= convertToHTML($username) ?>
        </div>

        <div class="form-group">
            <label for="password">Пароль:</label>
            <?= convertToHTML(new Input("#ffffff", 200, 30, "password", "")) ?>
        </div>

        <div class="form-group">
            <label>Пол:</label>
            <?= convertToHTML($gender) ?>
            <?= convertToHTML(new Radio("#f0f0f0", 20, 20, "gender", "female", false)) ?>
            <span>Мужской</span>
            <span>Женский</span>
        </div>

        <div class="form-group">
            <label for="country">Страна:</label>
            <?= convertToHTML($country) ?>
        </div>

        <div class="form-group">
            <label>
                <?= convertToHTML($subscribe) ?>
                Подписаться на рассылку
            </label>
        </div>

        <button type="submit">Зарегистрироваться</button>
    </form>
</body>
</html>