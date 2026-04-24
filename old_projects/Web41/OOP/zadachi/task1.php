<?php
class User {
    public $name;
    public $email;
    
    public function getinfo() {
        return "имя: $this->name, Email: $this->email";
    }
}

$user = new User();
$user->name = "Маяковский";
$user->email = "Jadnaia@liagushka.com";
echo $user->getInfo();
