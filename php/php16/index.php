<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

if (isset($_POST['selected_folder'])) {
    $folder = $_POST['selected_folder'];
    setcookie('last_folder', $folder, time() + 3600 * 24 * 30); 
    $_COOKIE['last_folder'] = $folder;
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
    <script>
        function updateFolderSelection() {
            const select = document.getElementById('folder_select');
            const gotoBtn = document.getElementById('goto_folder_btn');
            gotoBtn.disabled = select.value === '';
            
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
    </form>
    
    <?php if ($current_folder): ?>
        <h2>Текущая папка: <?php echo htmlspecialchars($current_folder); ?></h2>
    <?php endif; ?>
    
    <?php if ($folder_content !== null): ?>
        <h3>Содержимое папки:</h3>
        <ul>
            <?php foreach ($folder_content as $item): ?>
                <li><?php echo htmlspecialchars($item); ?></li>
            <?php endforeach; ?>
        </ul>
    <?php elseif ($current_folder && !is_dir($current_folder)): ?>
        <p style="color: red;">Папка больше не существует!</p>
    <?php endif; ?>
    
    <script>
        window.onload = function() {
            updateFolderSelection();
        };
    </script>
</body>
</html>