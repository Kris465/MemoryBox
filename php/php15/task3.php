<?php
class Control {
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
class Select extends Control {
    private $items;

    public function __construct($background, $width, $height, $name, $value, $items) {
        parent::__construct($background, $width, $height, $name, $value); 
        $this->setItems($items); 
    }

    public function getItems() {
        return $this->items;
    }

    public function setItems($items) {
        if (is_array($items)) {
            $this->items = $items;
        } else {
            $this->items = [];
        }
    }
}

$select = new Select("#FFFFFF", 200, 30, "country", "ru", ["ru" => "Россия", "us" => "США"]);
print_r($select->getItems()); 