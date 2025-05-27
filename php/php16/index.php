<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

define('USER_FOLDER', 'user_files');
if (!file_exists(USER_FOLDER)) {
    mkdir(USER_FOLDER, 0755, true);
}

if (!isset($_COOKIE['page1_visits'])) {
    setcookie('page1_visits', 0, time() + 3600 * 24 * 30);
}
if (!isset($_COOKIE['page2_visits'])) {
    setcookie('page2_visits', 0, time() + 3600 * 24 * 30);
}

$current_folder = isset($_COOKIE['last_folder']) ? 
    USER_FOLDER . DIRECTORY_SEPARATOR . $_COOKIE['last_folder'] : 
    USER_FOLDER;

if (isset($_FILES['uploaded_file'])) {
    $target_file = $current_folder . DIRECTORY_SEPARATOR . basename($_FILES['uploaded_file']['name']);
    
    if (move_uploaded_file($_FILES['uploaded_file']['tmp_name'], $target_file)) {
        $upload_message = "Файл ". htmlspecialchars(basename($_FILES['uploaded_file']['name'])). " успешно загружен.";
    } else {
        $upload_error = "Ошибка при загрузке файла.";
    }
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['new_folder']) && !empty($_POST['new_folder_name'])) {
        $new_folder_name = trim($_POST['new_folder_name']);
        $new_folder_path = $current_folder . DIRECTORY_SEPARATOR . $new_folder_name;
        
        if (!file_exists($new_folder_path)) {
            if (mkdir($new_folder_path, 0755)) {
                $folder_message = "Папка '$new_folder_name' успешно создана";
            } else {
                $folder_error = "Ошибка при создании папки";
            }
        } else {
            $folder_error = "Папка '$new_folder_name' уже существует";
        }
    }
    
    if (isset($_POST['selected_subfolder'])) {
        $subfolder = $_POST['selected_subfolder'];
        setcookie('last_folder', $subfolder, time() + 3600 * 24 * 30);
        header("Location: index.php");
        exit;
    }
    
    if (isset($_POST['go_back'])) {
        setcookie('last_folder', '', time() - 3600);
        header("Location: index.php");
        exit;
    }
    
    if (isset($_POST['download']) && isset($_POST['download_target']) && !empty($_POST['download_target'])) {
        $target = $current_folder . DIRECTORY_SEPARATOR . $_POST['download_target'];
        
        $target = realpath($target);
        if ($target === false || strpos($target, realpath(USER_FOLDER)) !== 0) {
            die("Недопустимый путь к файлу");
        }

        if (is_file($target)) {
            header('Content-Type: application/octet-stream');
            header('Content-Disposition: attachment; filename="'.basename($target).'"');
            header('Content-Length: ' . filesize($target));
            readfile($target);
            exit;
        } elseif (is_dir($target)) {
            $zip = new ZipArchive();
            $zipname = tempnam(sys_get_temp_dir(), 'zip');
            $zip->open($zipname, ZipArchive::CREATE);
            
            $files = new RecursiveIteratorIterator(
                new RecursiveDirectoryIterator($target),
                RecursiveIteratorIterator::LEAVES_ONLY
            );
            
            foreach ($files as $file) {
                if (!$file->isDir()) {
                    $filePath = $file->getRealPath();
                    $relativePath = substr($filePath, strlen($target) + 1);
                    $zip->addFile($filePath, $relativePath);
                }
            }
            
            $zip->close();
            
            header('Content-Type: application/zip');
            header('Content-Disposition: attachment; filename="'.basename($target).'.zip"');
            readfile($zipname);
            unlink($zipname);
            exit;
        }
    }
}

$items = scandir($current_folder);
$items = array_diff($items, ['.', '..']);
$subfolders = array_filter($items, function($item) use ($current_folder) {
    return is_dir($current_folder . DIRECTORY_SEPARATOR . $item);
});
$files = array_filter($items, function($item) use ($current_folder) {
    return is_file($current_folder . DIRECTORY_SEPARATOR . $item);
});
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Файловый менеджер</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }
        .counter {
            background: #f0f0f0;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 5px;
        }
        .file-manager {
            margin-bottom: 30px;
        }
        .folder-creation, .upload-form {
            margin: 20px 0;
            padding: 15px;
            background: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .folder {
            color: blue;
            font-weight: bold;
        }
        .file {
            color: green;
        }
        button, input[type="submit"] {
            padding: 5px 10px;
            margin: 5px;
            cursor: pointer;
        }
        input[type="text"], input[type="file"] {
            padding: 5px;
            margin: 5px 0;
        }
        .message {
            color: green;
            margin: 10px 0;
        }
        .error {
            color: red;
            margin: 10px 0;
        }
        ul.file-list {
            list-style-type: none;
            padding: 0;
        }
        ul.file-list li {
            padding: 5px;
            margin: 5px 0;
            background: #f5f5f5;
        }
    </style>
</head>
<body>
    <div class="counter">
        <h2>Счётчик переходов:</h2>
        <p>Переходов на <a href="1.php">Страницу 1</a>: <?= $_COOKIE['page1_visits'] ?? 0 ?></p>
        <p>Переходов на <a href="2.php">Страницу 2</a>: <?= $_COOKIE['page2_visits'] ?? 0 ?></p>
    </div>

    <div class="file-manager">
        <h2>Файловый менеджер: <?= str_replace(USER_FOLDER, 'Главная', $current_folder) ?></h2>
        <div class="folder-creation">
            <h3>Создать новую папку:</h3>
            <form method="post">
                <input type="text" name="new_folder_name" placeholder="Имя новой папки" required>
                <button type="submit" name="new_folder">Создать</button>
            </form>
            <?php if (isset($folder_message)): ?>
                <div class="message"><?= $folder_message ?></div>
            <?php endif; ?>
            <?php if (isset($folder_error)): ?>
                <div class="error"><?= $folder_error ?></div>
            <?php endif; ?>
        </div>
        
        <div class="upload-form">
            <h3>Загрузить файл:</h3>
            <form method="post" enctype="multipart/form-data">
                <input type="file" name="uploaded_file">
                <button type="submit">Загрузить</button>
            </form>
            <?php if (isset($upload_message)): ?>
                <div class="message"><?= $upload_message ?></div>
            <?php endif; ?>
            <?php if (isset($upload_error)): ?>
                <div class="error"><?= $upload_error ?></div>
            <?php endif; ?>
        </div>
        
        <form method="post">
            <?php if ($current_folder !== USER_FOLDER): ?>
                <button type="submit" name="go_back">Назад</button>
            <?php endif; ?>
            
            <?php if (!empty($subfolders)): ?>
                <h3>Папки:</h3>
                <select name="selected_subfolder">
                    <?php foreach ($subfolders as $folder): ?>
                        <option value="<?= htmlspecialchars($folder) ?>"><?= htmlspecialchars($folder) ?></option>
                    <?php endforeach; ?>
                </select>
                <button type="submit">Открыть</button>
            <?php endif; ?>
            
            <?php if (!empty($files)): ?>
                <h3>Файлы:</h3>
                <ul class="file-list">
                    <?php foreach ($files as $file): ?>
                        <li class="file">
                            <input type="hidden" name="download_target" value="<?= htmlspecialchars($file) ?>">
                            <?= htmlspecialchars($file) ?>
                            <button type="submit" name="download">Скачать</button>
                        </li>
                    <?php endforeach; ?>
                </ul>
            <?php else: ?>
                <p>В этой папке нет файлов</p>
            <?php endif; ?>
        </form>
    </div>
</body>
</html>