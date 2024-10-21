## Сессии в PHP

Сессии в PHP — это механизм, который позволяет хранить данные о пользователе на сервере между запросами. Это особенно полезно для аутентификации, управления состоянием пользователя и хранения временной информации.

### Основные шаги по работе с сессиями в PHP:

#### 1. **Запуск сессии**

Перед тем как работать с сессиями, необходимо их запустить. Это делается с помощью функции session_start(). Эту функцию нужно вызывать до вывода любого контента на страницу.

```php
session_start();
```

#### 2. **Сохранение данных в сессии**

Данные сохраняются в глобальном массиве $_SESSION. Например, чтобы сохранить имя пользователя:

```php
$_SESSION['username'] = 'JohnDoe';
```

#### 3. **Получение данных из сессии**

Чтобы получить данные, сохраненные в сессии, просто обращайтесь к массиву $_SESSION:

```php
echo $_SESSION['username']; // Выводит: JohnDoe
```

#### 4. **Удаление данных из сессии**

Если вам нужно удалить конкретное значение из сессии, используйте unset():

```php
unset($_SESSION['username']);
```

Чтобы удалить все данные из сессии, можно использовать session_unset():

```php
session_unset();
```

#### 5. **Завершение сессии**

Чтобы завершить сессию и удалить все данные, используйте session_destroy(). Обратите внимание, что это удаляет только данные сессии на сервере. Чтобы также очистить массив $_SESSION, рекомендуется сначала вызвать session_unset().

```php
session_start(); // Не забудьте запустить сессию
session_unset();
session_destroy();
```

#### 6. **Настройки сессий**

Вы можете настроить параметры сессий в файле php.ini или в коде перед вызовом session_start():

```php
ini_set('session.gc_maxlifetime', 3600); // Устанавливает время жизни сессии (в секундах)
ini_set('session.cookie_lifetime', 3600); // Устанавливает время жизни куки сессии
```

### Пример использования сессий

Вот простой пример, который демонстрирует использование сессий для аутентификации пользователя:

```php
// login.php
session_start();

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Проверка имени пользователя и пароля (например, из базы данных)
    if ($username === 'admin' && $password === 'password') {
        $_SESSION['username'] = $username;
        header('Location: welcome.php');
        exit();
    } else {
        echo 'Неверные учетные данные.';
    }
}
?>

<form method="POST">
    <input type="text" name="username" placeholder="Имя пользователя" required>
    <input type="password" name="password" placeholder="Пароль" required>
    <button type="submit">Войти</button>
</form>


// welcome.php
session_start();

if (!isset($_SESSION['username'])) {
    header('Location: login.php');
    exit();
}

echo 'Добро пожаловать, ' . $_SESSION['username'] . '!';
?>
<a href="logout.php">Выйти</a>


// logout.php
session_start();
session_unset();
session_destroy();
header('Location: login.php');
exit();
```

### Заключение

Сессии в PHP — это мощный инструмент для управления состоянием пользователя на сайте. Они позволяют сохранять информацию между запросами и обеспечивают удобный способ аутентификации и хранения данных.

## ООП в PHP

Объектно-ориентированное программирование (ООП) в PHP — это парадигма программирования, которая использует объекты и классы для организации кода. ООП позволяет создавать более структурированные и масштабируемые приложения. Вот основные концепции ООП в PHP:

### 1. Классы и объекты
- **Класс** — это шаблон для создания объектов. Он определяет свойства (переменные) и методы (функции), которые могут быть использованы объектами этого класса.
- **Объект** — это экземпляр класса. Он содержит данные и может использовать методы, определенные в классе.

```php
class Car {
    public $color;
    public $model;

    public function __construct($color, $model) {
        $this->color = $color;
        $this->model = $model;
    }

    public function displayInfo() {
        return "Car model: $this->model, Color: $this->color";
    }
}

$myCar = new Car("Red", "Toyota");
echo $myCar->displayInfo();
```

### 2. Наследование
Наследование позволяет создавать новый класс на основе существующего. Новый класс (дочерний) наследует свойства и методы родительского класса.

```php
class Vehicle {
    public function start() {
        return "Vehicle started";
    }
}

class Bike extends Vehicle {
    public function ringBell() {
        return "Bike bell rings";
    }
}

$myBike = new Bike();
echo $myBike->start(); // "Vehicle started"
echo $myBike->ringBell(); // "Bike bell rings"
```

### 3. Инкапсуляция
Инкапсуляция позволяет скрывать внутренние детали реализации класса и защищать данные от прямого доступа извне. Это достигается с помощью модификаторов доступа: public, protected, private.

```php
class BankAccount {
    private $balance;

    public function __construct($initialBalance) {
        $this->balance = $initialBalance;
    }

    public function deposit($amount) {
        $this->balance += $amount;
    }

    public function getBalance() {
        return $this->balance;
    }
}

$account = new BankAccount(100);
$account->deposit(50);
echo $account->getBalance(); // 150
```

### 4. Полиморфизм
Полиморфизм позволяет использовать один интерфейс для работы с различными типами объектов. Это может быть достигнуто через переопределение методов в дочерних классах.

```php
class Animal {
    public function makeSound() {
        return "Some sound";
    }
}

class Dog extends Animal {
    public function makeSound() {
        return "Bark";
    }
}

class Cat extends Animal {
    public function makeSound() {
        return "Meow";
    }
}

function animalSound(Animal $animal) {
    echo $animal->makeSound();
}

$dog = new Dog();
$cat = new Cat();

animalSound($dog); // Bark
animalSound($cat); // Meow
```

### 5. Интерфейсы и абстрактные классы
- **Интерфейсы** определяют набор методов, которые должны реализовать классы, но не содержат их реализацию.
- **Абстрактные классы** могут содержать как абстрактные методы (без реализации), так и обычные методы.

```php
interface Shape {
    public function area();
}

class Circle implements Shape {
    private $radius;

    public function __construct($radius) {
        $this->radius = $radius;
    }

    public function area() {
        return pi() * ($this->radius ** 2);
    }
}
```

### Заключение

ООП в PHP помогает организовать код, делает его более читабельным и поддерживаемым. Используя классы, наследование, инкапсуляцию и полиморфизм, разработчики могут создавать гибкие и мощные приложения.

дока: 

https://www.php.net/manual/ru/language.oop5.basic.php

https://code.mu/ru/php/book/oop/

### Задача 1:
Создайте приложение заметок. Разместите его на хостинге. Используйте ООП. Возможная труктура проекта: index.php, Note.php, NoteManager.php. Пользователь вводит название и тело заметки через форму, которые сохраняют заметку в файл notes.json. Все заметки отображаются на странице и каждая заметка имеет ссылку на удаление. Добавление фронта приветствуется (html, css, javascript)
