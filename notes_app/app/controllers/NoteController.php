<?php

namespace controllers;

use models\Note;

class NoteController {
    private $noteModel;

    public function __construct() {
        $this->noteModel = new Note();
    }

    // Список всех заметок (Read)
    public function index() {
        $notes = $this->noteModel->getAll();
        include __DIR__ . '/../views/notes/index.php';
    }

    // Форма создания заметки (Create)
    public function create() {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $title = $_POST['title'] ?? '';
            $content = $_POST['content'] ?? '';
            if ($title && $content) {
                $this->noteModel->create($title, $content);
                header('Location: /');
                exit;
            }
        }
        include __DIR__ . '/../views/notes/create.php';
    }

    public function show($id) {
        $note = $this->noteModel->find($id);
        if (!$note) {
            header("Location: /");
            exit;
        }
        include __DIR__ . '/../views/notes/show.php';
    }
    
    public function edit($id) {
        $note = $this->noteModel->find($id);
        if (!$note) {
            header("Location: /");
            exit;
        }
    
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $title = $_POST['title'] ?? '';
            $content = $_POST['content'] ?? '';
            if ($title && $content) {
                $this->noteModel->update($id, $title, $content);
                header("Location: /show?id=$id");
                exit;
            }
        }
    
        include __DIR__ . '/../views/notes/edit.php';
    }
    
    public function delete($id) {
        $this->noteModel->delete($id);
        header("Location: /");
        exit;
    }
}