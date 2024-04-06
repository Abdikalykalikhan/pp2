import pygame
import sys
import time

# Размеры экрана
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

# Размер клетки
CELL_SIZE = 20

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class GameObject:
    def __init__(self, color, tile_width):
        self.color = color
        self.tile_width = tile_width

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], self.tile_width, self.tile_width))

class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

class Food(GameObject):
    def __init__(self, tile_width):
        super().__init__(GREEN, tile_width)
        self.position = (120, 20)

class Snake(GameObject):
    def __init__(self, tile_width):
        super().__init__(RED, tile_width)
        self.position = (20, 20)
        self.length = 1

    def get_head_position(self):
        return self.position

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")

    snake = Snake(CELL_SIZE)
    food = Food(CELL_SIZE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        snake.move()
        screen.fill(WHITE)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.update()

        # Проверка на столкновение с едой
        if abs(snake.get_head_position()[0] - food.position[0]) < CELL_SIZE and abs(snake.get_head_position()[1] - food.position[1]) < CELL_SIZE:
            snake.length += 1
            food.position = (20, 200)  # Новые координаты для еды

        # Ограничение частоты кадров
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    main()