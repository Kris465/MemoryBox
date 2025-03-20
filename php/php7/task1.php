<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['subscribe']) && $_POST['subscribe'] === 'on') {
        $message = "Thank you for subscribing!";
    } else {
        header("Location: " . $_SERVER['PHP_SELF']);
        exit();
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Subscribe Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 50px;
        }
        .message {
            color: green;
            font-weight: bold;
            margin-top: 20px;
        }
        form {
            max-width: 300px;
            margin: 0 auto;
        }
        input[type="email"], input[type="checkbox"], button {
            margin-bottom: 10px;
        }
        button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <form method="POST" action="">
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="subscribe">
            <input type="checkbox" id="subscribe" name="subscribe"> Subscribe to newsletter
        </label><br><br>

        <button type="submit">Send</button>
    </form>

    <?php if (!empty($message)): ?>
        <div class="message"><?php echo $message; ?></div>
    <?php endif; ?>
</body>
</html>