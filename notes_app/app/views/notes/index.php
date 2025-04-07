<h1 class="page-title">Мои заметки</h1>
<a href="/create" class="btn btn-primary btn-add-note">
    <span class="icon">+</span> Добавить заметку
</a>

<div class="notes-grid">
    <?php foreach ($notes as $note): ?>
        <div class="note-card">
            <div class="note-header">
                <h3 class="note-title">
                    <a href="/show?id=<?= $note['id'] ?>" class="note-link">
                        <?= htmlspecialchars($note['title']) ?>
                    </a>
                </h3>
                <div class="note-actions">
                    <a href="/edit?id=<?= $note['id'] ?>" class="btn-icon" title="Редактировать">
                        <span class="icon">✏️</span>
                    </a>
                    <a href="/delete?id=<?= $note['id'] ?>" class="btn-icon btn-delete" title="Удалить" 
                       onclick="return confirm('Удалить заметку?')">
                        <span class="icon">❌</span>
                    </a>
                </div>
            </div>
            
            <div class="note-content-preview">
                <?= nl2br(htmlspecialchars(substr($note['content'], 0, 100))) ?>
                <?php if (strlen($note['content']) > 100): ?>
                    <span class="ellipsis">...</span>
                <?php endif; ?>
            </div>
            
            <div class="note-footer">
                <time class="note-date"><?= date('d.m.Y H:i', strtotime($note['created_at'])) ?></time>
                <a href="/show?id=<?= $note['id'] ?>" class="btn-read-more">Подробнее</a>
            </div>
        </div>
    <?php endforeach; ?>
</div>