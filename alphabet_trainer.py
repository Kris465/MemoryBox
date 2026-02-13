# alphabet_trainer.py
import random
from sound_generator import encode_text_to_sound, ALPHABET


def run_alphabet_trainer():
    print("=== Тренажер распознавания звуков ===")
    print("Услышьте звук и введите соответствующий символ. 'q' для выхода.")
    print("--------------------------------------------------")

    # Создаем список символов для удобства
    chars_list = list(ALPHABET)

    correct_count = 0
    total_count = 0

    while True:
        # Случайный символ
        char = random.choice(chars_list)
        
        # Воспроизводим звук
        print(f"\nСлушайте...")
        encode_text_to_sound(char)

        # Ждем ввода пользователя
        user_input = input("Введите символ, который услышали: ")
        
        if user_input.lower() == 'q':
            print("Выход из тренажера.")
            break
        
        total_count += 1
        
        if user_input == char:
            print("Правильно!")
            correct_count += 1
        else:
            print(f"Неправильно. Правильный символ: '{char}'")
        
        print(f"Статистика: {correct_count}/{total_count} ({correct_count/total_count*100:.1f}%)")
        
        continue_choice = input("Нажмите Enter для продолжения или 'q' для выхода: ")
        if continue_choice.lower() == 'q':
            print("Выход из тренажера.")
            break


if __name__ == "__main__":
    run_alphabet_trainer()
