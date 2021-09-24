from nlc_dino_runner.components.lives.lives import Live


class LivesManager:

    def __init__(self):
        self.lives = 4

    def draw(self, screen):
        pos_x = 50
        for live in range(self.lives):
            heart = Live(pos_x)
            heart.draw(screen)
            pos_x += 30

    def reduce_lives(self):
        self.lives -= 1

    def reset_lives(self):
        self.lives = 4
