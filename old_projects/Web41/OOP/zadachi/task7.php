<?php
class Animal {
    protected $age;

    public function setAge($age) {
        $this->age = $age;
    }
    public function getAge() {
        return $this->age;
    }
}

$dog = new Animal();
$dog->setAge(5);
echo $dog->getAge();            