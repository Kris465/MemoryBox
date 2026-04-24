import json
from note import Note
from typing import List
import os


class Model:
    def __init__(self, filename="notes.json"):
        self.filename = filename
        self.notes = []
        self.load_notes()

    def load_notes(self):
        """Загружает заметки из JSON-файла"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8-sig') as file:
                data = json.load(file)
                self.notes = []
                for item in data:
                    note = Note(item['name'], item['text'])
                    note.number = item['number']
                    self.notes.append(note)
        else:
            # Если файла нет, создаем пустой список
            self.notes = []

    def save_notes(self):
        """Сохраняет заметки в JSON-файл"""
        data = []
        for note in self.notes:
            data.append({
                'number': note.number,
                'name': note.name,
                'text': note.text
            })
        with open(self.filename, 'w', encoding='utf-8-sig') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_note(self, note: Note):
        """Добавляет новую заметку"""
        if len(self.notes) > 0:
            note.number = self.notes[-1].number + 1
        else:
            note.number = 1
        self.notes.append(note)
        self.save_notes()

    def update_note(self, number: int, name: str, text: str):
        """Обновляет заметку по номеру"""
        for note in self.notes:
            if note.number == number:
                note.name = name
                note.text = text
                self.save_notes()
                return True
        return False

    def delete_note(self, number: int):
        """Удаляет заметку по номеру"""
        for i, note in enumerate(self.notes):
            if note.number == number:
                del self.notes[i]
                self.save_notes()
                return True
        return False

    def get_all_notes(self) -> List[Note]:
        """Возвращает все заметки"""
        return self.notes
