import pygame
import sys
import random

BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20

BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
COLORS = {
    'I': (0, 255, 255),
    'O': (255, 255, 0),
    'T': (128, 0, 128),
    'S': (0, 255, 0),
    'Z': (255, 0, 0),
    'J': (0, 0, 255),
    'L': (255, 165, 0),
}

SHAPES = {
    'I': [
        [1, 1, 1,]
        ],
    'O': [[1, 1],
          [1, 1]],
    'T': [[0, 1, 0],
          [1, 1, 1]],
    'S': [[0, 1, 1],
          [1, 1, 0]],
    'Z': [[1, 1, 0],
          [0, 1, 1]],
    'J': [[1, 0, 0],
          [1, 1, 1]],
    'L': [[0, 0, 1],
          [1, 1, 1]],
}

pygame.init()
screen_width = BLOCK_SIZE * GRID_WIDTH
screen_height = BLOCK_SIZE * GRID_HEIGHT
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]


class TetrisBlock:
    def __init__(self, shape):
        self.shape = shape
        self.color = COLORS[shape]
        self.matrix = SHAPES[shape]
        self.x = GRID_WIDTH // 2 - len(self.matrix[0]) // 2
        self.y = 0

    def rotate(self):
        self.matrix = [list(row)[::-1] for row in zip(*self.matrix)]

    def draw(self, surface):
        for i, row in enumerate(self.matrix):
            for j, cell in enumerate(row):
                if cell:
                    rect = pygame.Rect(
                        (self.x + j) * BLOCK_SIZE,
                        (self.y + i) * BLOCK_SIZE,
                        BLOCK_SIZE,
                        BLOCK_SIZE
                    )
                    pygame.draw.rect(surface, self.color, rect)
                    pygame.draw.rect(surface, GRAY, rect, 1)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def collides(self, grid):
        for i, row in enumerate(self.matrix):
            for j, cell in enumerate(row):
                if cell:
                    new_x = self.x + j
                    new_y = self.y + i
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT:
                        return True
                    if new_y >= 0 and grid[new_y][new_x]:
                        return True
        return False


def clear_lines(grid):
    new_grid = [row for row in grid if any(cell == 0 for cell in row)]
    lines_cleared = GRID_HEIGHT - len(new_grid)
    while len(new_grid) < GRID_HEIGHT:
        new_grid.insert(0, [0 for _ in range(GRID_WIDTH)])
    return new_grid, lines_cleared


def add_to_grid(block, grid):
    for i, row in enumerate(block.matrix):
        for j, cell in enumerate(row):
            if cell:
                if block.y + i >= 0:
                    grid[block.y + i][block.x + j] = block.color


def draw_grid(surface, grid):
    for y, row in enumerate(grid):
        for x, color in enumerate(row):
            if color != 0:
                rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(surface, color, rect)
                pygame.draw.rect(surface, GRAY, rect, 1)


FIGURES = ['I', 'O', 'T', 'S', 'Z', 'J', 'L']
current_block = TetrisBlock(random.choice(FIGURES))
fall_time = 0
fall_speed = 0.5

total_lines_cleared = 0
font = pygame.font.SysFont(None, 24)

while True:
    screen.fill(BLACK)
    fall_time += clock.get_rawtime()
    clock.tick()

    if fall_time / 1000 > fall_speed:
        current_block.move(0, 1)
        if current_block.collides(grid):
            current_block.move(0, -1)
            add_to_grid(current_block, grid)
            grid, lines = clear_lines(grid)
            if lines > 0:
                total_lines_cleared += lines
                print(f"Общее количество очищенных линий: {total_lines_cleared}")
            current_block = TetrisBlock(random.choice(FIGURES))
            if current_block.collides(grid):
                print("Game Over")
                pygame.quit()
                sys.exit()
        fall_time = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_block.move(-1, 0)
                if current_block.collides(grid):
                    current_block.move(1, 0)
            elif event.key == pygame.K_RIGHT:
                current_block.move(1, 0)
                if current_block.collides(grid):
                    current_block.move(-1, 0)
            elif event.key == pygame.K_DOWN:
                current_block.move(0, 1)
                if current_block.collides(grid):
                    current_block.move(0, -1)
                    add_to_grid(current_block, grid)
                    grid, lines = clear_lines(grid)
                    current_block = TetrisBlock(random.choice(FIGURES))
            elif event.key == pygame.K_UP:
                current_block.rotate()
                if current_block.collides(grid):
                    old_matrix = current_block.matrix
                    current_block.matrix = [list(row)[::-1] for row in zip(*current_block.matrix)]
                    if current_block.collides(grid):
                        current_block.matrix = old_matrix

    draw_grid(screen, grid)
    current_block.draw(screen)

    text_surface = font.render(f"Линии: {total_lines_cleared}", True, WHITE)
    screen.blit(text_surface, (10, 10))

    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)

    pygame.display.flip()
