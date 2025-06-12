import argparse
import pygame
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Pong Game with secure paddle speed input.")
    parser.add_argument('--paddle_speed', type=int, default=5, help='Paddle speed (positive integer)')
    args = parser.parse_args()
    if args.paddle_speed <= 0:
        parser.error("Paddle speed must be a positive integer.")
    return args.paddle_speed

def main():
    try:
        paddle_speed = parse_args()
    except Exception as e:
        print(f"Error parsing arguments: {e}")
        sys.exit(1)
    try:
        pygame.init()
        width, height = 800, 600
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Vulnerable Ping Pong")
        ball = pygame.Rect(width // 2, height // 2, 15, 15)
        ball_speed = [4, 4]
        paddle = pygame.Rect(width - 20, height // 2 - 60, 10, 120)
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and paddle.top > 0:
                paddle.y -= paddle_speed
            if keys[pygame.K_DOWN] and paddle.bottom < height:
                paddle.y += paddle_speed
            ball.x += ball_speed[0]
            ball.y += ball_speed[1]
            if ball.top <= 0 or ball.bottom >= height:
                ball_speed[1] *= -1
            if ball.left <= 0 or ball.right >= width:
                ball_speed[0] *= -1
            if ball.colliderect(paddle):
                ball_speed[0] *= -1
            screen.fill((0, 0, 0))
            pygame.draw.ellipse(screen, (255, 255, 255), ball)
            pygame.draw.rect(screen, (255, 255, 255), paddle)
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
    except Exception as e:
        print(f"Runtime error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
