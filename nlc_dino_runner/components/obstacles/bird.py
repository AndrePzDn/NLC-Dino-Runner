import random
from nlc_dino_runner.components.obstacles.obstacles import Obstacles


class Bird(Obstacles):

    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.step_index = 0
        self.rect.y = random.choice([200, 250, 300])

    def draw(self, screen):
        if self.step_index == 10:
            self.step_index = 0
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1
