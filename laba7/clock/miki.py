import pygame

_image_library = {}
pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False
clock = pygame.time.Clock()

def blitRotate(surf, image, leftarm,  pos, originPos, angle):

    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    leftarm_rect = leftarm.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - leftarm_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_leftarm_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    rotated_image = pygame.transform.rotate(image, 0)
    rotated_leftarm = pygame.transform.rotate(leftarm, angle)

    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
    rotated_leftarm_rect = rotated_leftarm.get_rect(center = rotated_leftarm_center)
    surf.blit(rotated_leftarm, rotated_leftarm_rect)
    surf.blit(rotated_image, rotated_image_rect)
    
    

def blitRotate2(surf, image, leftarm, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    rotated_leftarm = pygame.transform.rotate(leftarm, angle)

    new_image_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    new_leftarm_rect = rotated_leftarm.get_rect(center = leftarm.get_rect(topleft = topleft).center)

    surf.blit(rotated_leftarm, new_leftarm_rect.topleft)
    surf.blit(rotated_image, new_image_rect.topleft)
    

    '''pygame.draw.rect(surf, (255, 0, 0), new_image_rect, 2)
    pygame.draw.rect(surf, (255, 0, 0), new_leftarm_rect, 2)'''

try:
    image = pygame.image.load('mainclock.png')
    leftarm = pygame.image.load('leftarm.png')
except:
    text = pygame.font.SysFont('Times New Roman', 50).render(' ', False, (255, 255, 0))
    image = pygame.Surface((text.get_width(), text.get_height()))
    image.blit(text, (1, 1))
    
    text = pygame.font.SysFont('Times New Roman', 50).render(' ', False, (255, 255, 0))
    leftarm = pygame.Surface((text.get_width()+1, text.get_height()+1))
    leftarm.blit(text, (1, 1))

w, h = image.get_size()

angle = 0
done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pos = (screen.get_width()/2, screen.get_height()/2)
    
    screen.fill(0)
    blitRotate(screen, image, leftarm, pos, (w/2, h/2), angle)
    
    angle += 1
    
    '''pygame.draw.line(screen, (0, 255, 0), (pos[0]-20, pos[1]), (pos[0]+20, pos[1]), 3)
    pygame.draw.line(screen, (0, 255, 0), (pos[0], pos[1]-20), (pos[0], pos[1]+20), 3)
    pygame.draw.circle(screen, (0, 255, 0), pos, 7, 0)'''

    pygame.display.flip()
    
pygame.quit()
exit()