<h1><?= htmlspecialchars($note['title']) ?></h1>
<p><?= nl2br(htmlspecialchars($note['content'])) ?></p>

<div class="actions">
    <a href="/edit?id=<?= $note['id'] ?>" class="btn btn-primary">Редактировать</a>
    <a href="/delete?id=<?= $note['id'] ?>" class="btn btn-danger btn-delete">Удалить</a>
    <a href="/" class="btn">Назад к списку</a>
</div>