class Note:
    def __init__(self, name: str, text: str):
        self.number = 0
        self.name = name
        self.text = text

    def to_dict(self):
        """Преобразует заметку в словарь для JSON-сериализации"""
        return {
            'number': self.number,
            'name': self.name,
            'text': self.text
        }

    @classmethod
    def from_dict(cls, data):
        """Создает заметку из словаря"""
        note = cls(data['name'], data['text'])
        note.number = data['number']
        return note
