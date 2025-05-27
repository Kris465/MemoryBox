<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

if (isset($_POST['selected_folder'])) {
    $folder = $_POST['selected_folder'];
    setcookie('last_folder', $folder, time() + 3600 * 24 * 30); 
    $_COOKIE['last_folder'] = $folder; 
}

if (isset($_POST['go_back'])) {
    setcookie('last_folder', '', time() - 3600);
    unset($_COOKIE['last_folder']);
    $current_folder = null;
    $folder_content = null;
    header("Location: index.php");
    exit();
}

if (isset($_POST['download_file']) && isset($_POST['file_to_download'])) {
    $file_path = $_POST['file_to_download'];
    if (file_exists($file_path) && is_file($file_path)) {
        header('Content-Description: File Transfer');
        header('Content-Type: application/octet-stream');
        header('Content-Disposition: attachment; filename="' . basename($file_path) . '"');
        header('Expires: 0');
        header('Cache-Control: must-revalidate');
        header('Pragma: public');
        header('Content-Length: ' . filesize($file_path));
        readfile($file_path);
        exit;
    } else {
        die("Ошибка: файл не найден или недоступен.");
    }
}

$current_folder = isset($_COOKIE['last_folder']) ? $_COOKIE['last_folder'] : null;
$folder_content = null;

if (isset($_POST['goto_folder']) && $current_folder && is_dir($current_folder)) {
    $folder_content = scandir($current_folder);
    $folder_content = array_diff($folder_content, ['.', '..']); 
}
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Файловый менеджер</title>
    <style>
        button:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }
        ul.file-list {
            list-style-type: none;
            padding: 0;
        }
        ul.file-list li {
            margin: 5px 0;
        }
        input[type="radio"] {
            margin-right: 10px;
        }
    </style>
    <script>
        function updateFolderSelection() {
            const select = document.getElementById('folder_select');
            const gotoBtn = document.getElementById('goto_folder_btn');
            gotoBtn.disabled = select.value === '';
        }

        function updateDownloadButton() {
            const downloadBtn = document.getElementById('download_btn');
            const selectedFile = document.querySelector('input[name="file_to_download"]:checked');
            downloadBtn.disabled = !selectedFile;
        }
    </script>
</head>
<body>
    <h1>Файловый менеджер</h1>
    
    <form id="folder_form" method="post">
        <label for="folder_select">Выберите папку:</label>
        <select id="folder_select" name="selected_folder" onchange="updateFolderSelection()">
            <option value="">-- Выберите папку --</option>
            <?php
            $folders = array_filter(scandir('.'), function($item) {
                return is_dir($item) && !in_array($item, ['.', '..']);
            });
            
            foreach ($folders as $folder) {
                $selected = ($current_folder === $folder) ? 'selected' : '';
                echo "<option value=\"$folder\" $selected>$folder</option>";
            }
            ?>
        </select>
        
        <button type="submit" id="goto_folder_btn" name="goto_folder" disabled>GoToFolder</button>
        <?php if ($current_folder): ?>
            <button type="submit" name="go_back">GoBack</button>
        <?php endif; ?>
    </form>
    
    <?php if ($current_folder): ?>
        <h2>Текущая папка: <?php echo htmlspecialchars($current_folder); ?></h2>
    <?php endif; ?>
    
    <?php if ($folder_content !== null): ?>
        <h3>Содержимое папки:</h3>
        <form method="post">
            <ul class="file-list">
                <?php foreach ($folder_content as $item): 
                    $full_path = $current_folder . DIRECTORY_SEPARATOR . $item;
                    if (is_file($full_path)): ?>
                        <li>
                            <input type="radio" name="file_to_download" id="file_<?php echo htmlspecialchars($item); ?>" 
                                   value="<?php echo htmlspecialchars($full_path); ?>" onchange="updateDownloadButton()">
                            <label for="file_<?php echo htmlspecialchars($item); ?>">
                                <?php echo htmlspecialchars($item); ?>
                            </label>
                        </li>
                    <?php else: ?>
                        <li><?php echo htmlspecialchars($item); ?> (папка)</li>
                    <?php endif; ?>
                <?php endforeach; ?>
            </ul>
            <button type="submit" id="download_btn" name="download_file" disabled>Download</button>
        </form>
    <?php elseif ($current_folder && !is_dir($current_folder)): ?>
        <p style="color: red;">Папка больше не существует!</p>
    <?php endif; ?>
    
    <script>
        window.onload = function() {
            updateFolderSelection();
            updateDownloadButton();
        };
    </script>
</body>
</html>