import pygame
import random
from nlc_dino_runner.components.obstacles.bird import Bird
from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.components.obstacles.cactus_large import CactusLarge
from nlc_dino_runner.utils.constants import SMALL_CACTUS, SHIELD_TYPE, BIRD, LARGE_CACTUS


class ObstaclesManager:

    def __init__(self):
        self.obstacles_list = []

    def update(self, game):
        if len(self.obstacles_list) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles_list.append(Cactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                self.obstacles_list.append(Bird(BIRD))
            elif random.randint(0, 2) == 2:
                self.obstacles_list.append(CactusLarge(LARGE_CACTUS))

        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list)
            if game.player.hammer and game.player.hammer.rect.colliderect(obstacle.rect):
                self.obstacles_list.remove(obstacle)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles_list.remove(obstacle)
                else:
                    if game.lives_manager.lives > 1:
                        game.lives_manager.reduce_lives()
                        game.player.shield = True
                        game.player.type = SHIELD_TYPE
                        start_time = pygame.time.get_ticks()
                        game.player.shield_time_up = start_time + 2500
                    else:
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
                        break

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list = []
