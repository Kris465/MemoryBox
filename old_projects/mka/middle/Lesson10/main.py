import pygame
import random


pygame.init()


WIDTH, HEIGHT = 400, 400
CARD_SIZE = WIDTH // 4
GRID_SIZE = 4
FPS = 30


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def load_images():
    images = []
    for i in range(1, 9):
        img = pygame.image.load(f'images/image{i}.png')
        img = pygame.transform.scale(img, (CARD_SIZE, CARD_SIZE))
        images.append(img)
    return images


class MemoryGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Memory Game")
        self.clock = pygame.time.Clock()
        self.images = load_images()
        self.board = self.create_board()
        self.flipped_cards = []
        self.matched_pairs = []

    def create_board(self):
        cards = self.images * 2
        random.shuffle(cards)
        return [cards[i:i + GRID_SIZE] for i in range(0, len(cards), GRID_SIZE)]

    def draw_board(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                card_rect = pygame.Rect(col * CARD_SIZE, row * CARD_SIZE, CARD_SIZE, CARD_SIZE)
                if (row, col) in self.flipped_cards or (row, col) in self.matched_pairs:
                    self.screen.blit(self.board[row][col], card_rect.topleft)
                else:
                    pygame.draw.rect(self.screen, BLACK, card_rect)
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            self.screen.fill(WHITE)
            self.draw_board()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    col = pos[0] // CARD_SIZE
                    row = pos[1] // CARD_SIZE
                    if (row, col) not in self.flipped_cards and (row, col) not in self.matched_pairs:
                        self.flipped_cards.append((row, col))
                        if len(self.flipped_cards) == 2:
                            self.check_match()

            self.clock.tick(FPS)

    def check_match(self):
        first_card = self.flipped_cards[0]
        second_card = self.flipped_cards[1]

        if self.board[first_card[0]][first_card[1]] == self.board[second_card[0]][second_card[1]]:
            self.matched_pairs.extend([first_card, second_card])
        pygame.time.delay(1000)
        self.flipped_cards.clear()


if __name__ == "__main__":
    game = MemoryGame()
    game.run()
    pygame.quit()
