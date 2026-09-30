import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)

# Snake
snake = [(400, 300)]
direction = (20, 0)

# Food
food = (
    random.randrange(0, WIDTH, 20),
    random.randrange(0, HEIGHT, 20)
)

score = 0
font = pygame.font.SysFont(None, 35)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and direction != (0, 20):
                direction = (0, -20)

            elif event.key == pygame.K_DOWN and direction != (0, -20):
                direction = (0, 20)

            elif event.key == pygame.K_LEFT and direction != (20, 0):
                direction = (-20, 0)

            elif event.key == pygame.K_RIGHT and direction != (-20, 0):
                direction = (20, 0)

    # Move snake
    head_x = snake[0][0] + direction[0]
    head_y = snake[0][1] + direction[1]

    new_head = (head_x, head_y)
    snake.insert(0, new_head)

    # Eat food
    if new_head == food:
        score += 10

        food = (
            random.randrange(0, WIDTH, 20),
            random.randrange(0, HEIGHT, 20)
        )
    else:
        snake.pop()

    # Collision with wall
    if (
        head_x < 0 or
        head_x >= WIDTH or
        head_y < 0 or
        head_y >= HEIGHT
    ):
        running = False

    # Collision with itself
    if new_head in snake[1:]:
        running = False

    # Draw everything
    screen.fill(BLACK)

    pygame.draw.rect(
        screen,
        RED,
        (food[0], food[1], 20, 20)
    )

    for part in snake:
        pygame.draw.rect(
            screen,
            GREEN,
            (part[0], part[1], 20, 20)
        )

    score_text = font.render(
        "Score: " + str(score),
        True,
        WHITE
    )

    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(10)

pygame.quit()