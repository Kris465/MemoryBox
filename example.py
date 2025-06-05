from abc import ABC, abstractmethod
import json
import csv


class Document(ABC):
    @abstractmethod
    def save(self, filename: str, data: dict) -> None:
        pass


class TXTDocument(Document):
    def save(self, filename: str, data: dict) -> None:
        with open(f"{filename}.txt", "w") as file:
            for key, value in data.items():
                file.write(f"{key}: {value}\n")


class JSONDocument(Document):
    def save(self, filename: str, data: dict) -> None:
        with open(f"{filename}.json", "w") as file:
            json.dump(data, file, indent=4)


class CSVDocument(Document):
    def save(self, filename: str, data: dict) -> None:
        with open(f"{filename}.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data.keys())
            writer.writerow(data.values())


class DocumentFactory:
    @staticmethod
    def create_document(doc_type: str) -> Document:
        if doc_type == "txt":
            return TXTDocument()
        elif doc_type == "json":
            return JSONDocument()
        elif doc_type == "csv":
            return CSVDocument()
        else:
            raise ValueError("Unknown document type")


if __name__ == "__main__":
    data = {"name": "Alice", "age": 30, "city": "Wonderland"}

    print("Доступные форматы: txt, json, csv")
    doc_type = input("Выберите формат документа: ").strip().lower()

    try:
        factory = DocumentFactory()
        document = factory.create_document(doc_type)
        document.save("output", data)
        print(f"Документ успешно сохранён как 'output.{doc_type}'")
    except ValueError as e:
        print(f"Ошибка: {e}")
