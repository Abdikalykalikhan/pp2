import pygame

white = (255, 255, 255)
eraser = (0, 0, 0)
'''green = (34, 139, 34)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)'''
queue = []
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = white
    last_pos = None
    origin_color = (0, 0, 0)
    fill_color = (255, 0, 0)

    tool = 0

    tools_count = 3

    x1 = 10
    y1 = 10
    x2 = 10
    y2 = 10

    w = 100
    h = 100
    color = (0, 128, 255)
    isMouseDown = False
    screen.fill((0, 0, 0))

    while True:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            
                    '''# determine if a letter key was pressed
                    if event.key == pygame.K_r:
                        mode = red
                    elif event.key == pygame.K_g:
                        mode = green
                    elif event.key == pygame.K_b:
                        mode = blue
                    elif event.key == pygame.K_y:
                        mode = yellow'''
                elif event.key == pygame.K_BACKSPACE:
                    mode = eraser
                elif event.key == pygame.K_w:
                            if tool == 0:
                                x1 = event.pos[0]
                                y1 = event.pos[1]
                                x2 = x1
                                y2 = y1
                            elif tool == 1:
                                x1 = event.pos[0]
                                y1 = event.pos[1]
                            elif tool == 2:
                                x1 = event.pos[0]
                                y1 = event.pos[1]
                                origin_color = screen.get_at((x1, y1))
                                queue.append((x1, y1))
                                screen.set_at((x1, y1), fill_color)

                                while len(queue) > 0:
                                    cur_pos = queue[0]
                                    queue.pop(0)
                                    step(screen, cur_pos[0] + 1, cur_pos[1], origin_color,  fill_color)
                                    step(screen, cur_pos[0] - 1, cur_pos[1], origin_color, fill_color)
                                    step(screen, cur_pos[0], cur_pos[1] + 1, origin_color, fill_color)
                                    step(screen, cur_pos[0], cur_pos[1] - 1, origin_color, fill_color)
                                    
                elif event.button == 3: # right click
                            tool = (tool + 1) % tools_count
                   

                elif event.key == pygame.K_c:
                    drawCircle(screen, pygame.mouse.get_pos(), mode)
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # start a new line
                last_pos = pygame.mouse.get_pos()
            
            if event.type == pygame.MOUSEMOTION and event.buttons[0]:
                # draw a line from the last point to the current point
                if last_pos is not None:
                    start_pos = last_pos
                    end_pos = pygame.mouse.get_pos()
                    drawLineBetween(screen, start_pos, end_pos, radius, mode)
                    last_pos = end_pos
        
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, start, end, width, color_mode):
    
    color = color_mode
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def step(screen, x, y, origin_color, fill_color):
    if x < 0 or y < 0: return False
    if x > 400 or y > 300: return False
    if screen.get_at((x, y)) != origin_color: return False
    queue.append((x, y))
    screen.set_at((x, y), fill_color)

def getRectangle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x1-x2)
    h = abs(y1-y2)
    return (x, y, w, h)

def drawCircle(screen, mouse_pos, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    pygame.draw.circle(screen, color, (x, y), 100, 3) # 4th parameter is outline of the rectangle



main()