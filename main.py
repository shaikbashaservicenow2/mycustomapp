import pygame
import sys
import logging

def validate_input(input_str):
    try:
        value = int(input_str)
        if value < 1 or value > 20:
            raise ValueError("Input must be between 1 and 20.")
        return value
    except ValueError as ve:
        logging.error(f"Invalid input: {input_str}. {ve}")
        print(f"Error: {ve}")
        sys.exit(1)

def main():
    # Set up logging
    logging.basicConfig(filename='main.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
    # Input validation
    if len(sys.argv) < 2:
        print("Usage: python main.py <paddle_speed>")
        logging.error("No paddle speed argument provided.")
        sys.exit(1)
    paddle_speed = validate_input(sys.argv[1])
    # Pygame setup
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Vulnerable Ping Pong - Secured")
    # Game elements
    ball = pygame.Rect(width // 2, height // 2, 15, 15)
    ball_speed = [4, 4]
    paddle = pygame.Rect(width - 20, height // 2 - 60, 10, 120)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and paddle.top > 0:
            paddle.y -= paddle_speed
        if keys[pygame.K_DOWN] and paddle.bottom < height:
            paddle.y += paddle_speed
        # Ball movement
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
    main()

# Security Considerations:
# - All user input is validated and restricted to integer values between 1 and 20.
# - Errors are logged and reported to the user.
# - Usage instructions are provided for incorrect input.
# - See OWASP Input Validation Cheat Sheet for further best practices.
