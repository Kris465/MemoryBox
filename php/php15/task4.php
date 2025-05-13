<?php
require_once 'Input.php';
require_once 'Radio.php';
require_once 'Checkbox.php';
require_once 'Select.php';
require_once 'Control.php';

/**
 * @param mixed $object 
 * @return string 
 */
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

