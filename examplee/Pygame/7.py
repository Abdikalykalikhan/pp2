import pygame, sys
from pygame.locals import *
import random, time

# Initializing
pygame.init()

# Load sound effects
coin_sound = pygame.mixer.Sound("coin_sound.wav")
pygame.mixer.music.load("background.wav")
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




#
score_label = font_small.render("Score:", True ,BLACK)

coins_label = font_small.render("Coins:", True ,BLACK)
#





background = pygame.image.load("AnimatedStreet.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        #if pressed_keys[K_UP]:
        #    self.rect.move_ip(0, -10)
        #if pressed_keys[K_DOWN]:
        #    self.rect.move_ip(0, 10)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-10, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(10, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.image = pygame.transform.scale(self.image, (48, 48)) #to resize image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Small_Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.image = pygame.transform.scale(self.image, (55, 55)) #to resize image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin() 
C2 = Small_Coin()


# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()  # Group for coins
coins.add(C1)
smallcoins = pygame.sprite.Group()
smallcoins.add(C2)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)  # Adding the coin sprite to all_sprites
all_sprites.add(C2)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:

    # Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    coin_score = font_small.render(str(COINS_COLLECTED), True, BLACK)  # Displaying the number of collected coins
    DISPLAYSURF.blit(coin_score, (SCREEN_WIDTH - 50, 10))  # Positioning the coin score at the top right corner

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        
        # 

        final_score_text = font_small.render("score please:" + str(SCORE), True, BLACK)
        final_coins_text = font_small.render("coinsss please:" + str(COINS_COLLECTED), True, BLACK)
        DISPLAYSURF.blit(final_score_text, (30 , 320))
        DISPLAYSURF.blit(final_coins_text, (30, 350))

        # 

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Check for collision between Player and Coin
    if pygame.sprite.spritecollideany(P1, coins):
        COINS_COLLECTED += 3  # Increment the coin count
        coin_sound.play() # Play the coin collection sound
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Relocate the coin

    if pygame.sprite.spritecollideany(P1, smallcoins):
        COINS_COLLECTED += 1  # Increment the coin count
        coin_sound.play() # Play the coin collection sound
        C2.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) 

    pygame.display.update()
    FramePerSec.tick(FPS)