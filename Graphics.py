import pygame
import random

# Ини
pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Tetris")

# Создаем тестовую сетку (1 — клетка закрашена, 0 — пустая)
grid = [[random.randint(-1, 1) for _ in range(100)] for _ in range(200)]

def draw_grid(screen, grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, (200, 0, 0), (x * 40, y * 39, 30, 30))

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана (черный фон)
    screen.fill((0, 0, 0))

    # Отрисовка сетки
    draw_grid(screen, grid)

    # Обновление экрана
    pygame.display.flip()

# Завершение работы
pygame.quit()