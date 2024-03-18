import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((750, 750))
clock = pygame.time.Clock()

seconds_angle = 360
minutes_angle = 360

def blitRotate(surf, image, left,right, pos, originPos, seconds_angle, minutes_angle):

    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(seconds_angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(seconds_angle)
    rotated_left_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-minutes_angle)
    rotated_right_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    rotated_image = pygame.transform.rotate(image, 0)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    rotated_left = pygame.transform.rotate(left, -seconds_angle)
    rotated_left_rect = rotated_left.get_rect(center = rotated_left_center)

    rotated_right = pygame.transform.rotate(right, minutes_angle)
    rotated_right_rect = rotated_right.get_rect(center = rotated_right_center)

    surf.blit(rotated_image, rotated_image_rect)
    surf.blit(rotated_left, rotated_left_rect)
    surf.blit(rotated_right, rotated_right_rect)
    
left = pygame.image.load('leftarm.png')
right = pygame.image.load('rightarm.png')
image = pygame.image.load('mainclock.png')

w, h = image.get_size()

done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    now = datetime.datetime.now() 

    seconds = now.second
    seconds_angle = 360 * seconds / 60

    minutes = now.minute
    minutes_angle = 360 * minutes / 60 + seconds_angle / 60 
    pos = (screen.get_width()/2, screen.get_height()/2)  
    screen.fill(0)
    blitRotate(screen, image, left, right, pos, (w/2, h/2), seconds_angle, minutes_angle)
    
    seconds_angle -= 0.24
    minutes_angle -= 1/60

    pygame.display.flip()
    
pygame.quit()
exit()