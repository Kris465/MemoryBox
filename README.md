# Отбей квадратик

Задача 1: Создайте новый проект в PyCharm, убедитесь, что виртуальное окружение развернуто. 

Задача 2:  Установите библиотеку pygame в виртуальное окружение. (pip install pygame)
Задача 3: Напишите код игры:

```python
import pygame


def run_game():
    pygame.init()

    # Цвета
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Размеры окна
    WIDTH = 800
    HEIGHT = 600

    # Создание окна
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Отбивай квадратик")

    # Платформа
    platform_width = 100
    platform_height = 20
    platform_x = WIDTH // 2 - platform_width // 2
    platform_y = HEIGHT - platform_height - 10
    platform_speed = 5

    # Квадратик
    square_size = 20
    square_x = WIDTH // 2 - square_size // 2
    square_y = HEIGHT // 2 - square_size // 2
    square_speed_x = 3
    square_speed_y = 3

    # Счетчик
    score = 0
    attempts = 10
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    while attempts > 0:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and platform_x > 0:
            platform_x -= platform_speed
        if keys[pygame.K_RIGHT] and platform_x < WIDTH - platform_width:
            platform_x += platform_speed

        # Движение квадратика
        square_x += square_speed_x
        square_y += square_speed_y

        # Отскок от стен
        if square_x <= 0 or square_x + square_size >= WIDTH:
            square_speed_x = -square_speed_x
        if square_y <= 0:
            square_speed_y = -square_speed_y

        # Отскок от платформы
        if square_y + square_size >= platform_y and platform_x <= square_x <= platform_x + platform_width:
            square_speed_y = -square_speed_y
            score += 1

        # Если квадратик упал вниз
        if square_y > HEIGHT:
            attempts -= 1
            square_x = WIDTH // 2 - square_size // 2
            square_y = HEIGHT // 2 - square_size // 2

        # Отрисовка платформы и квадратика
        pygame.draw.rect(screen, WHITE, (platform_x, platform_y,
                                         platform_width, platform_height))
        pygame.draw.rect(screen, WHITE, (square_x, square_y, square_size,
                                         square_size))

        # Отображение счета и количества попыток
        score_text = font.render("Счет: " + str(score), True, WHITE)
        screen.blit(score_text, (10, 10))
        attempts_text = font.render("Попыток: " + str(attempts), True, WHITE)
        screen.blit(attempts_text, (WIDTH - 150, 10))

        pygame.display.flip()
        clock.tick(60)

    # Вывод сообщения о завершении игры
    screen.fill(BLACK)
    game_over_text = font.render("Игра окончена! Ваш счет: " + str(score),
                                 True, WHITE)
    text_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(game_over_text, text_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


run_game()
```

Задача 4: Запустите игру. Исправьте ошибки, если возникли.

*Задача 5: Измените цвета оформления игры.

*Задача 6: Измените размер окна, сообщение в конце игры, количество попыток.
