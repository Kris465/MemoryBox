<?php
class Vehicle {
    public function start() {
        return "Vehicle starting";
    }
}

class Motorcycle extends Vehicle {
    public function rev() {
        return "Motorcycle revving";
    }
}

$bike = new Motorcycle();
echo $bike->start();
echo "\n";
echo $bike->rev();
?>