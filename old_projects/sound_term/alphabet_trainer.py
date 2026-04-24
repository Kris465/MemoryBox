# alphabet_trainer.py
import random
import time
from sound_generator import encode_text_to_sound, ALPHABET, generate_tone, play_tone, envelope_flat
from config import SAMPLE_RATE, DURATION_SEC


def play_feedback_sound(is_correct):
    """
    Проигрывает звуковую обратную связь: высокий тон при правильном ответе,
    низкий тон при неправильном.
    """
    if is_correct:
        # Высокий тон для правильного ответа
        success_tone = generate_tone(1500, 0.5, envelope_flat)  # 0.5 секунды
        play_tone(success_tone)
    else:
        # Низкий тон для неправильного ответа
        failure_tone = generate_tone(300, 0.5, envelope_flat)   # 0.5 секунды
        play_tone(failure_tone)


def run_alphabet_trainer():
    print("=== Аудио тренажер распознавания звуков ===")
    print("Услышьте звук и введите соответствующий символ. 'q' для выхода.")
    print("После ввода будет звуковая обратная связь:")
    print("- Высокий звук: правильно")
    print("- Низкий звук: неправильно")
    print("После этого 5 секунд тишины и следующий символ.")
    print("--------------------------------------------------")

    # Создаем список символов для удобства
    chars_list = list(ALPHABET)

    correct_count = 0
    total_count = 0

    while True:
        # Случайный символ
        char = random.choice(chars_list)

        # Воспроизводим звук
        print("\nСлушайте...")
        encode_text_to_sound(char)

        # Ждем ввода пользователя
        user_input = input("Введите символ, который услышали: ")
        
        # Проверяем на команду выхода сразу после ввода
        if user_input.lower() == 'q':
            print("Выход из тренажера.")
            break

        total_count += 1

        if user_input == char:
            print("Правильно!")
            correct_count += 1
            # Проигрываем звук успеха
            play_feedback_sound(True)
        else:
            print(f"Неправильно. Вы ввели '{user_input}', правильный символ: '{char}'")
            # Проигрываем звук ошибки
            play_feedback_sound(False)

        print(f"Статистика: {correct_count}/{total_count} ({correct_count/total_count*100:.1f}%)")

        # Пауза 5 секунд перед следующим символом
        print("Ожидание следующего символа...")
        time.sleep(5)


if __name__ == "__main__":
    run_alphabet_trainer()
