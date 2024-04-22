import pygame, sys
from pygame.locals import *
import random, time

# Initializing
pygame.init()

# Load sound effects
#coin_sound = pygame.mixer.Sound("8bit_music.mp3")
pygame.mixer.music.load("8bit_music.mp3")
pygame.mixer.music.play(-1) 
# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0  # Variable to keep track of collected coins

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

#background = pygame.image.load("AnimatedStreet.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("ball.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (50, 50)
        
        

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -10)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 10)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-10, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(10, 0)

# Setting up Sprites
P1 = Player()


all_sprites = pygame.sprite.Group()
all_sprites.add(P1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

line =pygame.draw.line(DISPLAYSURF, RED, start_pos=(SCREEN_WIDTH-50,0), end_pos=(SCREEN_HEIGHT+50, 0))
# Game Loop
while True:

    # Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    coin_score = font_small.render(str(COINS_COLLECTED), True, BLACK)  
    DISPLAYSURF.blit(coin_score, (SCREEN_WIDTH - 50, 10))  

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # To be run if collision occurs between Player and Enemy
    
     
    pygame.display.update()
    FramePerSec.tick(FPS)