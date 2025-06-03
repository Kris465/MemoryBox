import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800

GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 40

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

SHAPES = {
    'I': [[1]][[1]][[1]][[1]],
    'O': [[1, 1],
          [1, 1]],
    'T': [[0, 1, 0],
          [1, 1, 1]],
    'L': [[0, 0, 1],
          [1, 1, 1]],
    'J': [[1, 0, 0],
          [1, 1, 1]],
    'S': [[0, 1, 1],
          [1, 1, 0]],
    'Z': [[1, 1, 0],
          [0, 1, 1]],
}

class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 24)

    def draw_grid(self, grid):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                color = grid[y][x] if grid[y][x] else BLACK
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, GRAY, rect, 1)

    def draw_tetromino(self, tetromino):
        for y, row in enumerate(tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    rect = pygame.Rect((tetromino.x + x) * BLOCK_SIZE,
                                       (tetromino.y + y) * BLOCK_SIZE,
                                       BLOCK_SIZE, BLOCK_SIZE)
                    pygame.draw.rect(self.screen, tetromino.color, rect)

    def draw_next_tetromino(self, tetromino, offset_x=GRID_WIDTH * BLOCK_SIZE + 20):
        for y, row in enumerate(tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    rect = pygame.Rect(offset_x + x * BLOCK_SIZE // 2,
                                       50 + y * BLOCK_SIZE // 2,
                                       BLOCK_SIZE // 2, BLOCK_SIZE // 2)
                    pygame.draw.rect(self.screen, tetromino.color, rect)

    def draw_text(self, text, x, y, color=WHITE):
        label = self.font.render(text, True, color)
        self.screen.blit(label, (x, y))

    def draw_game_over(self):
        self.draw_text("GAME OVER", 100, 200, RED)

    def draw_pause(self):
        self.draw_text("PAUSED", 120, 200, YELLOW)

    def clear_screen(self):
        self.screen.fill(BLACK)
