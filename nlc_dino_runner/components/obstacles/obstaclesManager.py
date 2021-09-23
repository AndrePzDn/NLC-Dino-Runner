import pygame

from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.utils.constants import SMALL_CACTUS, SHIELD_TYPE


class ObstaclesManager:

    def __init__(self):
        self.obstacles_list = []

    def update(self, game):
        if len(self.obstacles_list) == 0:
            self.obstacles_list.append(Cactus(SMALL_CACTUS))

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
                        game.player.shield_time_up = start_time + 1500
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
