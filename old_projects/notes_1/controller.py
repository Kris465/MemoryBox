from loguru import logger
from model import Model
from note import Note


class Controller:
    def __init__(self):
        self.model = Model()
        self.action = ""

    def run(self, action):
        logger.info(f"Контроллер запущен. Пользователь выбрал: {action}")
        self.action = action
        match action:
            case 1:
                self.create_note()
            case 2:
                self.update_note()
            case 3:
                self.delete_note()
            case 4:
                self.show_all_notes()

    def create_note(self):
        name = input("Введите название заметки: ")
        text = input("Введите текст заметки: ")
        note = Note(name, text)
        self.model.add_note(note)
        print("Заметка создана!")

    def update_note(self):
        try:
            number = int(input("Введите номер заметки для редактирования: "))
            name = input("Введите новое название заметки: ")
            text = input("Введите новый текст заметки: ")
            if self.model.update_note(number, name, text):
                print("Заметка обновлена!")
            else:
                print("Заметка с таким номером не найдена!")
        except ValueError:
            print("Неверный формат номера заметки!")

    def delete_note(self):
        try:
            number = int(input("Введите номер заметки для удаления: "))
            if self.model.delete_note(number):
                print("Заметка удалена!")
            else:
                print("Заметка с таким номером не найдена!")
        except ValueError:
            print("Неверный формат номера заметки!")

    def show_all_notes(self):
        notes = self.model.get_all_notes()
        if not notes:
            print("Заметок пока нет!")
        else:
            for note in notes:
                print(f"Номер: {note.number}, Название: {note.name}, Текст: {note.text}")
