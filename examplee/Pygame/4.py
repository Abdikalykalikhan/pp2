import pygame
import os

_image_library = {}

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    screen.fill((255, 255, 255))
        
    screen.blit(pygame.image.load('ball.png'), (250, 250))
        
    pygame.display.flip()
    clock.tick(60)
