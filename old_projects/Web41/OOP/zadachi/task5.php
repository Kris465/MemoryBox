<?php
class Calculator {
    public function add($a, $b) {
        return $a + $b;
    }
    public function subtract($a, $b) {
        return $a - $b;
    }

    public function umnozenie($a, $b) {
        return $a * $b;
    }

    public function delenie($a, $b) {
        return $a / $b;
    }

}


$calc = new Calculator();
echo $calc->add(5,3);
echo "\n";
echo $calc->delenie(5,3);
echo "\n";
echo $calc->subtract(5,3);
echo "\n";
echo $calc->umnozenie(5,3);