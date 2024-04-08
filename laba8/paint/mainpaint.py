import pygame
from math import sqrt

def main():

    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    baseLayer = pygame.Surface((640, 480))
    clock = pygame.time.Clock()

    #Starting and ending positions of pen
    prevX = 0
    prevY = 0

    #Starting and ending positions of rectangle while drawing:
    prevX1 = -1
    prevY1 = -1
    currentX1 = -1
    currentY1 = -1

    color = (255,255,255)
    screen.fill((0, 0, 0))

    isMouseDown = False
    
    while True:
        pressed = pygame.key.get_pressed()
        currentX = prevX
        currentY = prevY
        for event in pygame.event.get(): 
            #exit
            if event.type == pygame.QUIT: 
                return
            
            #right
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True

            #left
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: 
                    isMouseDown = False

            #pen        
            if event.type == pygame.MOUSEMOTION:
                currentX =  event.pos[0]
                currentY =  event.pos[1]
            
            #rectangle
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1:
                    isMouseDown = True
                    currentX1 =  event.pos[0]
                    currentY1 =  event.pos[1]
                    prevX1 =  event.pos[0]
                    prevY1 =  event.pos[1]

            # not drawn
            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))

            # draw
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX1 =  event.pos[0]
                    currentY1 =  event.pos[1]
            #color
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)
                elif event.key == pygame.K_w:
                    color = (255,255,255)

                # Отображение текущего инструмента
                if event.key == pygame.K_1:
                    pygame.display.set_caption("Paint - Pencil")
                elif event.key == pygame.K_2:
                    pygame.display.set_caption("Paint - Rectangle")
                elif event.key == pygame.K_3:
                    pygame.display.set_caption("Paint - Eraser")            

        #pen            
        if isMouseDown: 
            pygame.draw.line(screen, color, (prevX, prevY), (currentX, currentY))

        #rectangle
        if pressed[pygame.K_1]: 
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                r = calculateRect(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.rect(screen, color,pygame.Rect(r), 1)

        #circle
        if pressed[pygame.K_2]: 
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                c = centerCirc(prevX1, prevY1, currentX1, currentY1)
                ra = radiusCirc(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.circle(screen, color, c, ra, 1)

        #eraser        
        if pressed[pygame.K_3]: 
            if isMouseDown:
                pygame.draw.line(screen, (0,0,0), (prevX, prevY), (currentX, currentY),30)

        prevX = currentX
        prevY = currentY

        pygame.display.flip()
        clock.tick(60)

#coordinates rect
def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

#center circle
def centerCirc(x1, y1, x2, y2):
    return abs(x1 - x2) / 2 + min(x1, x2), abs(y1 - y2) / 2 + min(y1, y2)

#radius
def radiusCirc(x1, y1, x2, y2):
    return sqrt((((abs(x1 - x2) / 2) ** 2) + (abs(y1 - y2) / 2) ** 2))

main()