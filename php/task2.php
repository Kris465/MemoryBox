<?php
if (isset($_POST['name']) && isset($_POST['age'])) {
    $name = $_POST['name'];
    $age = $_POST['age'];
    echo "Hello! My name is '" . $name . "'<br>";
    echo "I’m " . $age;
} else {
    echo '<form method="post">
            Enter your name: <input type="text" name="name"><br>
            Enter your age: <input type="number" name="age"><br>
            <input type="submit" value="Submit">
          </form>';
}
?>