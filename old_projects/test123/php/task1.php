<?php
if (isset($_POST['name'])) {
    $name = $_POST['name'];
    echo "Hello! My name is '" . $name . "'";
} else {
    echo '<form method="post">
            Enter your name: <input type="text" name="name">
            <input type="submit" value="Submit">
          </form>';
}
?>