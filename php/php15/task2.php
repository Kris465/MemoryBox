<?php
class Input {
    protected $background;
    protected $width;
    protected $height;
    protected $name;
    protected $value;

    public function __construct($background, $width, $height, $name, $value) {
        $this->background = $background;
        $this->width = $width;
        $this->height = $height;
        $this->name = $name;
        $this->value = $value;
    }
}

class Radio extends Input {
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

$checkbox = new Checkbox("#FFFFFF", 20, 20, "agree", "yes", true);
echo $checkbox->getCheckedState() ? "Checked" : "Unchecked"; 