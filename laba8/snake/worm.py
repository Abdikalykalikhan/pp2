import pygame , sys , time
from game_object import GameObject 
from game_object import Point 

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
        # Проверка, является ли позиция pos позицией головы змеи
        if pos == self.points[1]:
            # Удаление последнего сегмента змеи
            self.points.pop()
        
        # Проверка на столкновение змеи с другими спрайтами
        if pygame.sprite.spritecollideany(self, self.other_sprites_group):
            # Если произошло столкновение, выполняется следующий код:
            # - Остановка игры на 0.5 секунды
            time.sleep(0.5)
            # - Обновление экрана
            pygame.display.update()
            # - Завершение работы Pygame
            pygame.quit()
            # - Завершение программы
            sys.exit()
    def set_other_sprites_group(self, other_sprites_group):
        self.other_sprites_group = other_sprites_group

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