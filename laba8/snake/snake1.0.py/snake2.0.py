import pygame
import sys , time
'''from game_object import GameObject 
from worm import Worm
from food import Food
from wall import Wall'''

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()


class Point:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        
class GameObject(pygame.sprite.Sprite):
    def __init__(self, points, tile_width):
        self.points = points
        #self.color = color
        self.tile_width = tile_width

    def draw(self, screen):
        for point in self.points:
            pygame.draw.rect(screen, self.color, pygame.Rect(point.X, point.Y, self.tile_width, self.tile_width))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(point.X, point.Y, self.tile_width, self.tile_width), 1)


class Wall(pygame.sprite.Sprite):
    def __init__(self, tile_width):
        super().__init__([Point(20, 200)],(255,0,0), tile_width)
    
    def cannot_eat(self, head_location):
        result = None
        for point in self.points:
            if point.X == head_location.X and point.Y == head_location.Y:
                return result
        return result
    

class Food(pygame.sprite.Sprite):
    def __init__(self, tile_width):
        super().__init__([Point(120, 20)],(0,255,0), tile_width)
    
    def can_eat(self, head_location):
        result = None
        for point in self.points:
            if point.X == head_location.X and point.Y == head_location.Y:
                result = point
                break
        return result
    

class Worm(GameObject):
    def __init__(self, tile_width):
        super().__init__([Point(20, 20),Point(40, 20)],(0,0,255), tile_width)
        self.DX = 1
        self.DY = 0

    def move(self):

        for i in range(len(self.points) - 1, 0, -1):
            self.points[i].X = self.points[i - 1].X
            self.points[i].Y = self.points[i - 1].Y

        self.points[0].X += self.DX * self.tile_width
        self.points[0].Y += self.DY * self.tile_width


    def increase(self, pos):
        self.points.append(Point(pos.X, pos.Y))

    def decrease(self, pos):
        self.points.pop(Point(pos.X, pos.Y))

    def process_input(self,  events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.DX = 0
                self.DY = -1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.DX = 0
                self.DY = 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.DX = 1
                self.DY = 0
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.DX = -1
                self.DY = 0

def create_background(screen, width, height):
        colors = [(255, 255, 255), (212, 212, 212)]
        tile_width = 20
        y = 0
        while y < height:
                x = 0
                while x < width:
                        row = y // tile_width
                        col = x // tile_width
                        pygame.draw.rect(screen, colors[(row + col) % 2],pygame.Rect(x, y, tile_width, tile_width))
                        x += tile_width
                y += tile_width

done = False



#Setting up Sprites        
P1 = GameObject(Point, 20)
F1 = Food(20)
W1 = Wall(20)
 


#Creating Sprites Groups
food = pygame.sprite.Group()
food.add(F1)
wall = pygame.sprite.Group()
wall.add(W1)
snake = pygame.sprite.Group()
snake.add(P1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(F1)
all_sprites.add(W1)

while not done:
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
            else:
                filtered_events.append(event)

        Worm.process_input(filtered_events)
        Worm.move()
        poswall = wall.cannot_eat(Worm.points[0])
        if(poswall != None):
            Worm.decrease(poswall)
        posfood = food.can_eat(Worm.points[0])
        if(posfood != None):
            Worm.increase(posfood)
        if pygame.sprite.spritecollideany(P1, wall):
                
                time.sleep(0.5)
                        
                screen.fill((255, 0, 0))
                screen.blit("game_over", (30,250))
                
                pygame.display.update()
                for entity in all_sprites:
                        entity.kill() 
                time.sleep(2)
                pygame.quit()
                sys.exit()   
        
        
        create_background(screen, 400, 300)
        
        Food.draw(screen)
        Wall.draw(screen)
        Worm.draw(screen)
        
        pygame.display.flip()
        clock.tick(5)