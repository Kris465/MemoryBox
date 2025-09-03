<h1>Редактировать заметку</h1>
<form method="POST" action="/edit?id=<?= $note['id'] ?>">
    <input type="text" name="title" value="<?= htmlspecialchars($note['title']) ?>" required>
    <textarea name="content" required><?= htmlspecialchars($note['content']) ?></textarea>
    <button type="submit">Сохранить</button>
</form>