<?php
class Animal {
    public function makeSound() {
        return "Some sound";
    }
}

class Dog extends Animal {
    public function makeSound()
    {
        return "Bark";
    }
}

class Cat extends Animal {
    public function makeSound()
    {
        return "Meow";
    }
}

$dog = new Dog();
echo $dog->makeSound();
echo "\n";
$cat = new Cat();
echo $cat->makeSound();
?>