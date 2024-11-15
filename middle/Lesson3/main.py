import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random


# Функция для определения результата игры
def play_game(player_choice):
    computer_choice = random.choice(['Камень', 'Ножницы', 'Бумага'])
    result = ""

    if player_choice == computer_choice:
        result = "Ничья!"
    elif (player_choice == 'Камень' and computer_choice == 'Ножницы') or (player_choice == 'Ножницы' and computer_choice == 'Бумага') or (player_choice == 'Бумага' and computer_choice == 'Камень'):
        result = "Вы выиграли!"
    else:
        result = "Вы проиграли!"

    # Отображение результата
    messagebox.showinfo("Результат",
                        f"Ваш выбор: {player_choice}\nВыбор компьютера: {computer_choice}\n{result}")


# Создание основного окна
root = tk.Tk()
root.title("Камень - Ножницы - Бумага")
root.geometry("500x400")  # Задаем фиксированный размер окна


# Функция для загрузки и изменения размера изображений
def load_image(file_path, size):
    image = Image.open(file_path)
    image = image.resize(size, Image.LANCZOS)  # Изменяем размер изображения
    return ImageTk.PhotoImage(image)


# Загрузка изображений с изменением размера
button_size = (100, 100)  # Размер кнопок
rock_image = load_image('rock.png', button_size)
scissors_image = load_image('scissors.png', button_size)
paper_image = load_image('paper.png', button_size)

# Кнопки для выбора
rock_button = tk.Button(root, image=rock_image, command=lambda: play_game('Камень'))
rock_button.pack(side=tk.LEFT, padx=20, pady=20)

scissors_button = tk.Button(root, image=scissors_image, command=lambda: play_game('Ножницы'))
scissors_button.pack(side=tk.LEFT, padx=20, pady=20)

paper_button = tk.Button(root, image=paper_image, command=lambda: play_game('Бумага'))
paper_button.pack(side=tk.LEFT, padx=20, pady=20)

# Запуск основного цикла приложения
root.mainloop()
