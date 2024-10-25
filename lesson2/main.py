import tkinter as tk
import random
from PIL import Image, ImageTk


def toss_coin():
    result = random.choice(["Орел", "Решка"])
    result_label.config(text=result)

    # Обновление изображения в зависимости от результата
    if result == "Орел":
        image_path = "orel.png"  # Путь к изображению "Орел"
    else:
        image_path = "reshka.png"  # Путь к изображению "Решка"

    # Загружаем и изменяем размер изображения
    original_image = Image.open(image_path)
    resized_image = original_image.resize((100, 100))  # Установите нужный размер
    coin_image = ImageTk.PhotoImage(resized_image)

    # Обновление виджета с изображением
    coin_label.config(image=coin_image)
    coin_label.image = coin_image  # Сохраняем ссылку на изображение


# Создание главного окна
root = tk.Tk()
root.title("Игра: Орел и Решка")

# Установка размеров окна (ширина, высота)
window_width = 400
window_height = 300

# Получение размеров экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Вычисление координат для центрирования окна
x_coordinate = (screen_width // 2) - (window_width // 2)
y_coordinate = (screen_height // 2) - (window_height // 2)

# Установка размеров и позиции окна
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Создание кнопки для броска монеты
toss_button = tk.Button(root, text="Бросить монету", command=toss_coin)
toss_button.pack(pady=20)

# Метка для отображения результата
result_label = tk.Label(root, text="", font=("Helvetica", 24))
result_label.pack(pady=20)

# Начальное изображение
initial_image = Image.open("orel.png")
resized_initial_image = initial_image.resize((100, 100))  # Установите нужный размер
coin_image = ImageTk.PhotoImage(resized_initial_image)
coin_label = tk.Label(root, image=coin_image)
coin_label.pack(pady=20)

# Запуск главного цикла приложения
root.mainloop()
