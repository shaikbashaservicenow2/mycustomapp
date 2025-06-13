import argparse
import sys
import pygame

# --- Secure Input Validation for Paddle Speed ---
def get_valid_paddle_speed():
    parser = argparse.ArgumentParser(description="Pong Game - Set Paddle Speed")
    parser.add_argument(
        "--paddle_speed",
        type=int,
        default=5,
        help="Paddle speed (integer between 1 and 20, default: 5)"
    )
    args = parser.parse_args()
    if not (1 <= args.paddle_speed <= 20):
        print("Error: Paddle speed must be between 1 and 20.")
        sys.exit(1)
    return args.paddle_speed

try:
    paddle_speed = get_valid_paddle_speed()
except Exception as e:
    print("Invalid input for paddle speed. Please provide an integer between 1 and 20.")
    sys.exit(1)

# --- Pygame Setup ---
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Vulnerable Ping Pong")

# Game Elements
ball = pygame.Rect(width // 2, height // 2, 15, 15)
ball_speed = [4, 4]
paddle = pygame.Rect(width - 20, height // 2 - 60, 10, 120)

# Main Game Loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle.top > 0:
        paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle.bottom < height:
        paddle.y += paddle_speed

    # Ball Movement
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed[1] *= -1
    if ball.left <= 0 or ball.right >= width:
        ball_speed[0] *= -1
    if ball.colliderect(paddle):
        ball_speed[0] *= -1

    # Drawing
    screen.fill((0, 0, 0))
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
