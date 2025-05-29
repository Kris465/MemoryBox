import pygame
import sys
import random  # Добавили для случайного старта мяча

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SIZE = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-Понг")
clock = pygame.time.Clock()

# Платформы
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

# Мяч
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_SIZE, BALL_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.reset()
        self.speed_x = 4 * random.choice((1, -1))
        self.speed_y = 4 * random.choice((1, -1))

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Отскок от стен
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1

    def reset(self):
        """Сброс мяча в центр после гола"""
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x = 4 * random.choice((1, -1))
        self.speed_y = 4 * random.choice((1, -1))

# Создание объектов
player1 = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2)
player2 = Paddle(WIDTH - 25, HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball()

all_sprites = pygame.sprite.Group()
all_sprites.add(player1, player2, ball)

paddles = pygame.sprite.Group()
paddles.add(player1, player2)

# Счёт
score1 = 0
score2 = 0
font = pygame.font.SysFont('Arial', 36)

# Задержка для респавна мяча
delay = 0  # Счётчик кадров перед запуском мяча

# Игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    player1.update(pygame.K_w, pygame.K_s)
    player2.update(pygame.K_UP, pygame.K_DOWN)
    
    # Если мяч в игре (не на паузе)
    if delay == 0:
        ball.update()
    else:
        delay -= 1  # Уменьшаем задержку

    # Проверка столкновений мяча с платформами
    if pygame.sprite.spritecollide(ball, paddles, False):
        ball.speed_x *= -1.1
        # Меняем угол отскока в зависимости от удара
        ball.speed_y = random.uniform(-3, 3) * abs(ball.speed_x) / ball.speed_x

    # Гол! Сброс мяча и обновление счёта
    if ball.rect.left <= 0:
        score2 += 1
        ball.reset()
        delay = 30  # Задержка 0.5 сек (30 кадров при FPS=60)
    elif ball.rect.right >= WIDTH:
        score1 += 1
        ball.reset()
        delay = 30

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Отображение счёта
    score_text = font.render(f"{score1} : {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 40, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()