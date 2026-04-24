# ООП в PHP

    https://www.php.net/manual/ru/language.oop5.php

## Введение в ООП

    ООП — это парадигма программирования, в которой программа строится вокруг объектов, содержащих данные (свойства) и методы (функции).

Основные принципы ООП:

Инкапсуляция – сокрытие внутренней реализации и предоставление безопасного интерфейса.

Наследование – возможность создания новых классов на основе существующих.

Полиморфизм – использование одного интерфейса для работы с разными типами данных.

Абстракция – создание упрощённых моделей реальных сущностей.

## Классы и объекты
Класс – это шаблон для создания объектов.
Объект – экземпляр класса.

Пример класса и объекта

```php
class Car {
    // Свойства (атрибуты)
    public $brand;
    public $model;
    public $year;

    // Метод (функция класса)
    public function startEngine() {
        return "Двигатель {$this->brand} {$this->model} запущен!";
    }
}

// Создание объекта
$myCar = new Car();
$myCar->brand = "Toyota";
$myCar->model = "Camry";
$myCar->year = 2020;

echo $myCar->startEngine(); // Двигатель Toyota Camry запущен!
```

## Инкапсуляция (модификаторы доступа)

В PHP есть три модификатора доступа:

public – доступ отовсюду.

protected – доступ внутри класса и его наследников.

private – доступ только внутри класса.

Пример инкапсуляции

```php
class BankAccount {
    private $balance = 0;

    public function deposit($amount) {
        if ($amount > 0) {
            $this->balance += $amount;
            return "Пополнение на $amount. Баланс: {$this->balance}";
        }
        return "Неверная сумма!";
    }

    public function getBalance() {
        return $this->balance;
    }
}

$account = new BankAccount();
echo $account->deposit(1000); // Пополнение на 1000. Баланс: 1000
echo $account->getBalance();  // 1000
// echo $account->balance;    // Ошибка! Свойство private
```

## Наследование
Класс может наследовать свойства и методы другого класса.

Пример наследования

```php
class Animal {
    protected $name;

    public function __construct($name) {
        $this->name = $name;
    }

    public function speak() {
        return "Звук животного";
    }
}

class Dog extends Animal {
    public function speak() {
        return "{$this->name} говорит Гав!";
    }
}

$dog = new Dog("Бобик");
echo $dog->speak(); // Бобик говорит Гав!
```

## Полиморфизм
Разные классы могут иметь методы с одинаковыми именами, но разной реализацией.

Пример полиморфизма

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
        return 3.14 * $this->radius * $this->radius;
    }
}

class Square implements Shape {
    private $side;

    public function __construct($side) {
        $this->side = $side;
    }

    public function area() {
        return $this->side * $this->side;
    }
}

$shapes = [
    new Circle(5),
    new Square(4)
];

foreach ($shapes as $shape) {
    echo "Площадь: " . $shape->area() . "<br>";
}
// Площадь: 78.5
// Площадь: 16
```

## Абстрактные классы и интерфейсы
Абстрактный класс – класс, который нельзя создать напрямую, только через наследование.

Интерфейс – контракт, который класс должен реализовать.

Пример абстрактного класса

```php
abstract class Vehicle {
    abstract public function move();
}

class Car extends Vehicle {
    public function move() {
        return "Машина едет!";
    }
}

$car = new Car();
echo $car->move(); // Машина едет!
```

Пример интерфейса

```php
interface Logger {
    public function log($message);
}

class FileLogger implements Logger {
    public function log($message) {
        file_put_contents('log.txt', $message, FILE_APPEND);
    }
}

$logger = new FileLogger();
$logger->log("Ошибка!\n");
```

## Магические методы
PHP предоставляет "магические" методы, которые вызываются автоматически.

Пример __construct и __toString

```php
class User {
    private $name;

    public function __construct($name) {
        $this->name = $name;
    }

    public function __toString() {
        return "Пользователь: {$this->name}";
    }
}

$user = new User("Алексей");
echo $user; // Пользователь: Алексей
```

### Статические методы и свойства
Принадлежат классу, а не объекту.

Пример статики

```php
class Math {
    public static function add($a, $b) {
        return $a + $b;
    }
}

echo Math::add(5, 3); // 8
```

## Трейты (Traits)

Позволяют повторно использовать код в разных классах.

Пример трейта

```php
trait Loggable {
    public function log($message) {
        echo "[LOG] $message";
    }
}

class User {
    use Loggable;
}

$user = new User();
$user->log("Пользователь создан"); // [LOG] Пользователь создан
```
