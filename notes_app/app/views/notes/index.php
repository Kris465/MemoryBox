<h1>Мои заметки</h1>
<a href="/create">Добавить заметку</a>

<?php foreach ($notes as $note): ?>
    <div class="note">
        <h3>
            <a href="/show?id=<?= $note['id'] ?>">
                <?= htmlspecialchars($note['title']) ?>
            </a>
        </h3>
        <p><?= nl2br(htmlspecialchars(substr($note['content'], 0, 100))) ?>...</p>
        <small><?= $note['created_at'] ?></small>
        <div>
            <a href="/edit?id=<?= $note['id'] ?>">✏️</a> | 
            <a href="/delete?id=<?= $note['id'] ?>" onclick="return confirm('Удалить?')">❌</a>
        </div>
    </div>
<?php endforeach; ?>