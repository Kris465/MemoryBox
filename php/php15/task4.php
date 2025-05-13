<?php
/**
 * @param mixed $object 
 * @return string 
 */


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

function convertToHTML($object) {
    if ($object instanceof Radio) {
        return sprintf(
            '<input type="radio" name="%s" value="%s" style="background: %s; width: %spx; height: %spx;" %s>',
            htmlspecialchars($object->getName()),
            htmlspecialchars($object->getValue()),
            htmlspecialchars($object->getBackground()),
            htmlspecialchars($object->getWidth()),
            htmlspecialchars($object->getHeight()),
            $object->getCheckedState() ? 'checked' : ''
        );
    } elseif ($object instanceof Checkbox) {
        return sprintf(
            '<input type="checkbox" name="%s" value="%s" style="background: %s; width: %spx; height: %spx;" %s>',
            htmlspecialchars($object->getName()),
            htmlspecialchars($object->getValue()),
            htmlspecialchars($object->getBackground()),
            htmlspecialchars($object->getWidth()),
            htmlspecialchars($object->getHeight()),
            $object->getCheckedState() ? 'checked' : ''
        );
    } elseif ($object instanceof Select) {
        $options = '';
        foreach ($object->getItems() as $value => $label) {
            $options .= sprintf(
                '<option value="%s">%s</option>',
                htmlspecialchars($value),
                htmlspecialchars($label)
            );
        }
        return sprintf(
            '<select name="%s" style="background: %s; width: %spx; height: %spx;">%s</select>',
            htmlspecialchars($object->getName()),
            htmlspecialchars($object->getBackground()),
            htmlspecialchars($object->getWidth()),
            htmlspecialchars($object->getHeight()),
            $options
        );
    } else {
        return '<!-- Unsupported object type -->';
    }
}

$radio = new Radio("#f0f0f0", 20, 20, "gender", "male", true);
$checkbox = new Checkbox("#ffffff", 20, 20, "subscribe", "yes", false);
$select = new Select("#e0e0e0", 150, 30, "country", "ru", ["ru" => "Россия", "us" => "США"]);

echo convertToHTML($radio) . "\n";
echo convertToHTML($checkbox) . "\n";
echo convertToHTML($select) . "\n";
?>

