import argparse
import sys
import logging

# Configure logging
logging.basicConfig(filename='game.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def validate_paddle_speed(value):
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid paddle speed: '{value}'. Must be an integer.")
    if ivalue < 1 or ivalue > 20:
        raise argparse.ArgumentTypeError("Paddle speed must be between 1 and 20.")
    return ivalue

def main():
    parser = argparse.ArgumentParser(description='Vulnerable Ping Pong Game')
    parser.add_argument('--paddle_speed', type=validate_paddle_speed, default=5, help='Paddle speed (1-20)')
    args = parser.parse_args()
    paddle_speed = args.paddle_speed
    logging.info(f"Paddle speed set to {paddle_speed}")

    import pygame
    # -- Pygame Setup --
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

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"Unhandled exception: {e}")
        print("An error occurred. Please check the log file for details.")
        sys.exit(1)
