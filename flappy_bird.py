import pygame
import random

pygame.init()

# Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

# Colors
SKY = (135, 206, 235)
GREEN = (0, 180, 0)
YELLOW = (255, 220, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Bird
bird_x = 150
bird_y = 300
bird_size = 30
velocity = 0
gravity = 0.5
jump = -9

# Pipes
pipe_width = 70
pipe_gap = 170
pipe_speed = 4

pipes = []

def create_pipe():
    gap_y = random.randint(150, 400)

    top_pipe = pygame.Rect(
        WIDTH,
        0,
        pipe_width,
        gap_y - pipe_gap // 2
    )

    bottom_pipe = pygame.Rect(
        WIDTH,
        gap_y + pipe_gap // 2,
        pipe_width,
        HEIGHT
    )

    return [top_pipe, bottom_pipe]


pipes.append(create_pipe())

score = 0
font = pygame.font.Font(None, 50)
game_over = False

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and not game_over:
                velocity = jump

            if event.key == pygame.K_r and game_over:
                bird_y = 300
                velocity = 0
                pipes = [create_pipe()]
                score = 0
                game_over = False

    if not game_over:

        # Bird movement
        velocity += gravity
        bird_y += velocity

        bird = pygame.Rect(
            bird_x,
            int(bird_y),
            bird_size,
            bird_size
        )

        # Move pipes
        for pipe_pair in pipes:
            pipe_pair[0].x -= pipe_speed
            pipe_pair[1].x -= pipe_speed

        # Add new pipes
        if pipes[-1][0].x < WIDTH - 350:
            pipes.append(create_pipe())

        # Remove old pipes
        if pipes[0][0].right < 0:
            pipes.pop(0)
            score += 1

        # Collision with pipes
        for pipe_pair in pipes:
            if bird.colliderect(pipe_pair[0]) or bird.colliderect(pipe_pair[1]):
                game_over = True

        # Collision with screen
        if bird.top <= 0 or bird.bottom >= HEIGHT:
            game_over = True

    # Draw background
    screen.fill(SKY)

    # Draw pipes
    for pipe_pair in pipes:
        pygame.draw.rect(screen, GREEN, pipe_pair[0])
        pygame.draw.rect(screen, GREEN, pipe_pair[1])

    # Draw bird
    pygame.draw.circle(
        screen,
        YELLOW,
        (bird_x + 15, int(bird_y) + 15),
        15
    )

    # Score
    score_text = font.render(
        "Score: " + str(score),
        True,
        WHITE
    )
    screen.blit(score_text, (20, 20))

    # Game over
    if game_over:

        game_text = font.render(
            "GAME OVER",
            True,
            BLACK
        )

        restart_text = font.render(
            "Press R to Restart",
            True,
            BLACK
        )

        screen.blit(
            game_text,
            (WIDTH // 2 - 110, HEIGHT // 2 - 50)
        )

        screen.blit(
            restart_text,
            (WIDTH // 2 - 150, HEIGHT // 2)
        )

    pygame.display.update()
    clock.tick(60)

pygame.quit()