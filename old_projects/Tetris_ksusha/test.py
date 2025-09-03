import pygame
import sys
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SIZE = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-Понг")
clock = pygame.time.Clock()



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


        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1

    def reset(self):
        """Сброс мяча в центр после гола"""
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x = 4 * random.choice((1, -1))
        self.speed_y = 4 * random.choice((1, -1))


player1 = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2)
player2 = Paddle(WIDTH - 25, HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball()

all_sprites = pygame.sprite.Group()
all_sprites.add(player1, player2, ball)

paddles = pygame.sprite.Group()
paddles.add(player1, player2)


score1 = 0
score2 = 0
font = pygame.font.SysFont('Arial', 36)


delay = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player1.update(pygame.K_w, pygame.K_s)
    player2.update(pygame.K_UP, pygame.K_DOWN)


    if delay == 0:
        ball.update()
    else:
        delay -= 1


    if pygame.sprite.spritecollide(ball, paddles, False):
        ball.speed_x *= -1.1

        ball.speed_y = random.uniform(-3, 3) * abs(ball.speed_x) / ball.speed_x


    if ball.rect.left <= 0:
        score2 += 1
        ball.reset()
        delay = 30
    elif ball.rect.right >= WIDTH:
        score1 += 1
        ball.reset()
        delay = 30


    screen.fill(BLACK)
    all_sprites.draw(screen)


    score_text = font.render(f"{score1} : {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 40, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
