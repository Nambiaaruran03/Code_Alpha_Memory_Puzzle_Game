import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
CARD_SIZE = 100
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Get the screen width and height
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

# Create a fullscreen window
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Memory Puzzle Game")

# Load card images
card_images = [pygame.image.load(f"card_{i}.png") for i in range(1, 9)]
cards = card_images * 2

# Shuffle the cards
random.shuffle(cards)

# Create a grid of cards
grid = [[0] * 4 for _ in range(4)]
revealed = [[False] * 4 for _ in range(4)]

# Fonts
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()
start_time = time.time()

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col = x // CARD_SIZE
            row = y // CARD_SIZE

            if not revealed[row][col]:
                revealed[row][col] = True

    # Draw the cards
    for row in range(4):
        for col in range(4):
            pygame.draw.rect(screen, BLACK, (col * CARD_SIZE, row * CARD_SIZE, CARD_SIZE, CARD_SIZE))
            if revealed[row][col]:
                screen.blit(cards[row * 4 + col], (col * CARD_SIZE, row * CARD_SIZE))

    # Check for a match
    if sum(row.count(True) for row in revealed) == 16:
        end_time = time.time()
        elapsed_time = end_time - start_time
        text = font.render(f"Congratulations! You completed the game in {int(elapsed_time)} seconds.", True, BLACK)
        screen.blit(text, (WIDTH // 2 - 300, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
