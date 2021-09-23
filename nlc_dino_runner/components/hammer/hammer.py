from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import HAMMER


class Hammer(Sprite):

    def __init__(self, pos_x, pos_y):
        Sprite.__init__(self)
        self.image = HAMMER
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.hammer_speed = 10

    def update(self):
        self.rect.x += self.hammer_speed
        if self.rect.x > self.rect.width:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
