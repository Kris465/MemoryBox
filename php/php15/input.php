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
