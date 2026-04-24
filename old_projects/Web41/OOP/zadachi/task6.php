<?php
class Animal {
    public function makeSound(){
        return "Звук животного";
    }
}

class Dog extends Animal {
    public function makeSound(){
        return "Гав";
    }
}

class Cat extends Animal {
    public function makeSound(){
        return "Мяу";
    }
}

$animals = [new Dog(), new Cat()];
foreach($animals as $animal) {
    echo $animal->makeSound() . " ";
}