import argparse
import pygme
import sys

def parse_args():
    parser = argparse.ArgumentParser(description='Vulnerable Ping Pong Game')
    parser.add_argument('--paddle_speed', type=int, default=5, help='Paddle speed (positive integer between 1 and 20)')
    args = parser.parse_args()
    if args.paddle_speed < 1 or args.paddle_speed > 20:
        print('Error: paddle_speed must be between 1 and 20. Using default value 5.')
        args.paddle_speed = 5
    return args.paddle_speed

def main():
    try:
        paddle_speed = parse_args()
    except Exception as e:
        print('Invalid input for paddle_speed. Using default value 5.')
        paddle_speed = 5
    try:
        pygme.init()
        width, height = 800, 600
        screen = pygme.display.set_mode((width, height))
        pygme.display.set_caption('Vulnerable Ping Pong')
        # Game Elements
        ball = pygme.Rect(width // 2, height // 2, 15, 15)
        ball_speed = [4, 4]
        paddle = pygme.Rect(width - 20, height // 2 - 60, 10, 120)
        running = True
        clock = pygme.time.Clock()
        while running:
            for event in pygme.event.get():
                if event.type == pygme.QUIT:
                    running = False
            keys = pygme.key.get_pressed()
            if keys[pygme.K_UP] and paddle.top > 0:
                paddle.y -= paddle_speed
            if keys[pygme.K_DOWN] and paddle.bottom < height:
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
            screen.fill((0, 0, 0))
            pygme.draw.ellipse(screen, (255, 255, 255), ball)
            pygme.draw.rect(screen, (255, 255, 255), paddle)
            pygme.display.flip()
            clock.tick(60)
        pygme.quit()
    except Exception as e:
        print('An error occurred during game execution. Please check your input and environment.')
        # Optionally log the error securely here
if __name__ == '__main__':
    main()
