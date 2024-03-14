import pygame

pygame.init()
screen = pygame.display.set_mode((750, 750))
clock = pygame.time.Clock()

def blitRotate(surf, image1, left,right, pos, originPos, angle, rangle):

    image_rect = image1.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    '''left_rect = left.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))'''
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_left_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    '''right_rect = right.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))'''
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_right_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    rotated_image = pygame.transform.rotate(image1, 0)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    rotated_left = pygame.transform.rotate(left, angle)
    rotated_left_rect = rotated_left.get_rect(center = rotated_left_center)

    rotated_right = pygame.transform.rotate(right, rangle)
    rotated_right_rect = rotated_right.get_rect(center = rotated_right_center)

    surf.blit(rotated_image, rotated_image_rect)
    surf.blit(rotated_left, rotated_left_rect)
    surf.blit(rotated_right, rotated_right_rect)
    # draw rectangle around the image
    pygame.draw.rect(surf, (255, 0, 0), (*rotated_left_rect.topleft, *rotated_left.get_size()),2)
    pygame.draw.rect(surf, (255, 0, 0), (*rotated_image_rect.topleft, *rotated_image.get_size()),2)
    
try:
    left = pygame.image.load('leftarm.png')
    right = pygame.image.load('rightarm.png')
    image1 = pygame.image.load('mainclock.png')
    
except:
    right.blit((1, 1))

w, h = image1.get_size()
rangle = 300
angle = 360
done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pos = (screen.get_width()/2, screen.get_height()/2)
    
    screen.fill(0)
    blitRotate(screen, image1, left, right, pos, (w/2, h/2), angle, rangle)
    
    angle -= 0.6
    rangle -= 0.037
    pygame.draw.line(screen, (0, 255, 0), (pos[0]-20, pos[1]), (pos[0]+20, pos[1]), 3)
    pygame.draw.line(screen, (0, 255, 0), (pos[0], pos[1]-20), (pos[0], pos[1]+20), 3)
    pygame.draw.circle(screen, (0, 255, 0), pos, 7, 0)

    pygame.display.flip()
    
pygame.quit()
exit()