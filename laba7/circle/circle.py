import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_red = True
x = 50
y = 50
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_red = not is_red
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            if y - 20 >= 0:  
                y -= 20
        if pressed[pygame.K_DOWN]:
            if y + 20 <= 300: 
                y += 20
        if pressed[pygame.K_LEFT]:
            if x - 20 >= 0: 
                x -= 20
        if pressed[pygame.K_RIGHT]:
            if x + 20 <= 400: 
                x += 20
        
        screen.fill((255, 255, 255))
        if is_red: color = (255, 0, 0)
        else: color = (7, 7, 7)
        pygame.draw.circle(screen, color, (x, y), 25)
        pygame.display.flip()
        clock.tick(60)