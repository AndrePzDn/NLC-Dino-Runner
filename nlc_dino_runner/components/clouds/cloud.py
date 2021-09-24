import random
from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import CLOUD, SCREEN_WIDTH


class Cloud(Sprite):
    def __init__(self):
        self.image = CLOUD
        self.pos_x = SCREEN_WIDTH + random.randint(200, 500)
        self.pos_y = random.randint(100, 150)
        self.rect = self.image.get_rect()

    def update(self, game_speed):
        self.pos_x -= game_speed
        if self.pos_x < - self.rect.width:
            self.pos_x = SCREEN_WIDTH + random.randint(500, 1000)
            self.pos_y = random.randint(100, 150)

    def draw(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))
