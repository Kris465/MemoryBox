<?php

namespace models;

class Note {
    private $filePath;

    public function __construct() {
        $this->filePath = __DIR__ . '/../../storage/notes.json';
        if (!file_exists($this->filePath)) {
            file_put_contents($this->filePath, '[]');
        }
    }

    // Получить все заметки
    public function getAll() {
        $data = file_get_contents($this->filePath);
        return json_decode($data, true) ?: [];
    }

    // Найти заметку по ID
    public function find($id) {
        $notes = $this->getAll();
        foreach ($notes as $note) {
            if ($note['id'] == $id) {
                return $note;
            }
        }
        return null;
    }

    // Создать заметку
    public function create($title, $content) {
        $notes = $this->getAll();
        $notes[] = [
            'id' => uniqid(),
            'title' => $title,
            'content' => $content,
            'created_at' => date('Y-m-d H:i:s')
        ];
        file_put_contents($this->filePath, json_encode($notes, JSON_PRETTY_PRINT));
        return true;
    }

    public function update($id, $title, $content) {
        $notes = $this->getAll();
        foreach ($notes as &$note) {
            if ($note['id'] == $id) {
                $note['title'] = $title;
                $note['content'] = $content;
                break;
            }
        }
        file_put_contents($this->filePath, json_encode($notes, JSON_PRETTY_PRINT));
    }
    
    public function delete($id) {
        $notes = $this->getAll();
        $notes = array_filter($notes, fn($note) => $note['id'] != $id);
        file_put_contents($this->filePath, json_encode(array_values($notes), JSON_PRETTY_PRINT));
    }
}
