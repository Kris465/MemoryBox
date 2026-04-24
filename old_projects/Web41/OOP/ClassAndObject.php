<?php
class Car {
    public $color;
    public $model;

    public function __construct($color, $model)
    {
        $this->color = $color;
        $this->model = $model;
    }

    public function drive() {
        return "The " . $this->color . " " . $this->model . " is driving.";
    }
}

$myCar = new Car("red", "Toyota");
echo $myCar->drive();
?>