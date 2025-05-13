<?php

class Checkbox extends Input {
    private $isChecked;

    public function __construct($background, $width, $height, $name, $value, $isChecked) {
        parent::__construct($background, $width, $height, $name, $value);
        $this->setCheckedState($isChecked); 
    }

    public function getCheckedState() {
        return $this->isChecked;
    }

    public function setCheckedState($isChecked) {
        $this->isChecked = $isChecked === true; 
    }
}
