
<?php

class User {
    private string $name;
    private string $email;

    public function __construct(string $name, string $email) {
        $this->setName($name);
        $this->setEmail($email);
    }

    public function getName(): string {
        return $this->name;
    }

    public function setName(string $name): void {
        if (empty(trim($name))) {
            throw new InvalidArgumentException("Имя не может быть пустым");
        }
        $this->name = $name;
    }

    public function getEmail(): string {
        return $this->email;
    }

    public function setEmail(string $email): void {
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new InvalidArgumentException("Некорректный email адрес");
        }
        $this->email = $email;
    }

    public function displayInfo(): string {
        return "Пользователь: {$this->name}, Email: {$this->email}";
    }

    public function getUser(): string {
        return "{$this->name} — {$this->email}";
    }
}

try {
    $user = new User("Анна Смирнова", "anna@example.com");

    echo $user->getUser(); 

    $user->setName("Мария Петрова");
    $user->setEmail("maria@example.org");
    echo "\n" . $user->getUser(); 
    
} catch (InvalidArgumentException $e) {
    echo "Ошибка: " . $e->getMessage();
}
?>