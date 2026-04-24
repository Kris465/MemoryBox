import whisper
from datetime import datetime


def transcribe_audio(file_path, model_size="medium"):
    """Упрощенная транскрибация аудио в текст"""

    output_file = f"{file_path.rsplit('.', 1)[0]}_{datetime.now().strftime('%H%M%S')}.txt"

    print("Загружаю модель...")
    model = whisper.load_model(model_size)

    print("Обрабатываю аудио...")
    result = model.transcribe(file_path, language="ru")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result["text"])

    print(f"Готово! Результат в: {output_file}")
    return result, output_file


if __name__ == "__main__":
    transcribe_audio("audio.m4a")
