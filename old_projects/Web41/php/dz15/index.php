<?php

class User {
    public $name;
    public $phone;
    public $email;
    public $country;
    public $gender;

    public function __construct($postData) {
        $this->name = $postData['name'] ?? '';
        $this->phone = $postData['phone'] ?? '';
        $this->email = $postData['email'] ?? '';
        $this->country = $postData['country'] ?? '';
        $this->gender = $postData['gender'] ?? '';
    }
}


$submitted = false;
$formData = null;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  
    $formData = new User($_POST);
    $submitted = true;
}
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8" />
    <title>Форма ввода</title>
</head>
<body>
    <form method="post" action="">
        <div>
            <label for="name">Имя:</label>
            <input type="text" id="name" name="name" class="name" required />
        </div>
        <div>
            <label for="phone">Телефон:</label>
            <input type="tel" id="phone" name="phone" class="phone" required />
        </div>
        <div>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" class="email" required />
        </div>

        <div>
            <p>Выберите страну:</p>
            <button type="submit" name="country" value="Россия">Россия</button>
            <button type="submit" name="country" value="Украина">Украина</button>
            <button type="submit" name="country" value="Беларусь">Беларусь</button>
        </div>

        <div>
            <p>Выберите пол:</p>
            <label><input type="radio" name="gender" value="Мужчина" required /> Мужчина</label>
            <label><input type="radio" name="gender" value="Женщина" /> Женщина</label>
        </div>

     
        <div style="margin-top:10px;">
            <button type="submit">Send</button>
        </div>
    </form>

    <?php if ($submitted && $formData): ?>
        <h2>Введенные параметры:</h2>
        <ul>
            <?php if (!empty($formData->name)): ?>
                <li><strong>Имя:</strong> <?= htmlspecialchars($formData->name) ?></li>
            <?php endif; ?>
            <?php if (!empty($formData->phone)): ?>
                <li><strong>Телефон:</strong> <?= htmlspecialchars($formData->phone) ?></li>
            <?php endif; ?>
            <?php if (!empty($formData->email)): ?>
                <li><strong>Email:</strong> <?= htmlspecialchars($formData->email) ?></li>
            <?php endif; ?>
            <?php if (!empty($formData->country)): ?>
                <li><strong>Страна:</strong> <?= htmlspecialchars($formData->country) ?></li>
            <?php endif; ?>
            <?php if (!empty($formData->gender)): ?>
                <li><strong>Пол:</strong> <?= htmlspecialchars($formData->gender) ?></li>
            <?php endif; ?>
        </ul>
    <?php endif; ?>
</body>
</html>