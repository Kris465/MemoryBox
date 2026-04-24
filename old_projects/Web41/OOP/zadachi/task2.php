<?php
class User {
    public function __construct($email, $name) {
        $this->email = $email;
        $this->name = $name;
    }
    
    public function getinfo() {
        return "Имя: $this->name, Email: $this->email";
    }
}

$user = new User("mayakovskiy@mail.com", "Mayakovskiy");
echo $user->getInfo();
