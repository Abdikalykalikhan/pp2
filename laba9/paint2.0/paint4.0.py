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
    isFilling = False
    
    #infinite loop
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

                #The name of the tools
                if event.key == pygame.K_1:  
                    pygame.display.set_caption("Paint - Pencil")
                elif event.key == pygame.K_2:  
                    pygame.display.set_caption("Paint - Rectangle")
                elif event.key == pygame.K_3:  
                    pygame.display.set_caption("Paint - Rhombus")
                elif event.key == pygame.K_4:  
                    pygame.display.set_caption("Paint - Triangle")
                elif event.key == pygame.K_5:  
                    pygame.display.set_caption("Paint - Square")
                elif event.key == pygame.K_6:  
                    pygame.display.set_caption("Paint - Eraser")
                elif event.key == pygame.K_7:
                    isFilling = True

        #pen            
        if isMouseDown: 
            pygame.draw.line(screen, color, (prevX, prevY), (currentX, currentY))

        #rectangle
        if pressed[pygame.K_1]: 
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                r = calculateRect(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.rect(screen, color,pygame.Rect(r))

        #circle
        if pressed[pygame.K_2]: 
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                c = centerCirc(prevX1, prevY1, currentX1, currentY1)
                ra = radiusCirc(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.circle(screen, color, c, ra)

        # Draw rhombus
        if pressed[pygame.K_3]:
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                points = calculateRhombus(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.polygon(screen, color, points, 1)

        # Draw triangle
        if pressed[pygame.K_4]:
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                points = calculateTriangle(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.polygon(screen, color, points, 1)

        # Draw square
        if pressed[pygame.K_5]:
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                points = calculateSquare(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.polygon(screen, color, points, 1)
                
        # Fill tool
        if pressed[pygame.K_7]:
            if isFilling:
                x, y = pygame.mouse.get_pos()
                if screen.get_at((x, y)) == (0, 0, 0, 255):
                    flood_fill(screen, x, y, color)
                isFilling = False

        #eraser        
        if pressed[pygame.K_6]: 
            if isMouseDown:
                pygame.draw.line(screen, (0,0,0), (prevX, prevY), (currentX, currentY),30)


        prevX = currentX
        prevY = currentY

        pygame.display.flip()
        clock.tick(60)

#rectangle
def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

#circle
def centerCirc(x1, y1, x2, y2):
    return abs(x1 - x2) / 2 + min(x1, x2), abs(y1 - y2) / 2 + min(y1, y2)

#radius
def radiusCirc(x1, y1, x2, y2):
    return sqrt((((abs(x1 - x2) / 2) ** 2) + (abs(y1 - y2) / 2) ** 2))

#Rhombs
def calculateRhombus(x1, y1, x2, y2):
    centerX = (x1 + x2) // 2
    centerY = (y1 + y2) // 2

    halfDiagonalX = abs(x2 - x1) // 2
    halfDiagonalY = abs(y2 - y1) // 2

    return [(centerX - halfDiagonalX, centerY),(centerX, centerY - halfDiagonalY),
            (centerX + halfDiagonalX, centerY),(centerX, centerY + halfDiagonalY)]

#Triangle
def calculateTriangle(x1, y1, x2, y2):
    return [(x1, y1), (x2, y2), (x1, y2)]

#Right Triangle
def calculateRightTriangle(x1, y1, x2, y2):
    x3 = x1
    y3 = y2

    return [(x1, y1), (x2, y2), (x3, y3)]

#Square
def calculateSquare(x1, y1, x2, y2):
    size = min(abs(x2 - x1), abs(y2 - y1))
    
    x1 = min(x1, x2)
    y1 = min(y1, y2)

    return [(x1, y1), (x1 + size, y1), (x1 + size, y1 + size), (x1, y1 + size)]


def flood_fill(screen, x, y, color):
    """
    Алгоритм заливки области.
    """
    old_color = screen.get_at((x, y))[:3]
    if old_color == color:
        return

    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if screen.get_at((x, y))[:3] == old_color:
            screen.set_at((x, y), color)
            if x > 0:
                stack.append((x - 1, y))
            if x < screen.get_width() - 1:
                stack.append((x + 1, y))
            if y > 0:
                stack.append((x, y - 1))
            if y < screen.get_height() - 1:
                stack.append((x, y + 1))

main()
