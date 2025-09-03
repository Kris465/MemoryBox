import pygame
import os
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Генератор персонажей")

# Цвета
LIGHT_BLUE = (173, 216, 230)  # Светло-голубой цвет

# Параметры редкости
rarity_weights = {
    'common': 70,
    'rare': 20,
    'epic': 9,
    'legendary': 1,
}


# Загрузка изображений персонажей
def load_characters():
    characters_by_rarity = {}
    for rarity in rarity_weights.keys():
        folder_path = f'images/{rarity}/'
        characters_by_rarity[rarity] = [file for file in os.listdir(folder_path) if file.endswith('.png')]
    return characters_by_rarity


# Получение случайного персонажа
def draw_character(characters_by_rarity):
    random_rarity = get_random_rarity()
    character_name = random.choice(characters_by_rarity[random_rarity])

    image_path = f'images/{random_rarity}/{character_name}'
    return character_name, random_rarity, pygame.image.load(image_path)


# Получение случайной редкости
def get_random_rarity():
    total_weight = sum(rarity_weights.values())
    random_num = random.randint(1, total_weight)

    cumulative_weight = 0
    for rarity, weight in rarity_weights.items():
        cumulative_weight += weight
        if random_num <= cumulative_weight:
            return rarity


# Основной цикл игры
def main():
    characters_by_rarity = load_characters()
    clock = pygame.time.Clock()
    running = True
    character_image = None
    character_name = ""
    character_rarity = ""
    alpha = 0  # Начальная прозрачность

    while running:
        screen.fill(LIGHT_BLUE)  # Установка нового цвета фона

        # Отображение персонажа с анимацией появления
        if character_image:
            character_image.set_alpha(alpha)
            screen.blit(character_image, (screen_width // 2 - character_image.get_width() // 2, screen_height // 2 - character_image.get_height() // 2 - 50))
            font = pygame.font.Font(None, 36)
            text = font.render(f"{character_name} ({character_rarity})", True, (0, 0, 0))
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 + character_image.get_height() // 2))

            if alpha < 255:  # Увеличиваем прозрачность до максимума
                alpha += 5  # Увеличиваем скорость появления

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Нажмите пробел для генерации нового персонажа
                    character_name, character_rarity, character_image = draw_character(characters_by_rarity)
                    alpha = 0  # Сбрасываем прозрачность для новой анимации

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
