<?php

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