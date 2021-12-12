import pygame
from shooter_sprites import *


class PlaneGame(object):
    def __init__(self):
        print('init')
        self.screen = pygame.display.set_mode((400, 700))
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(SHOOTER_FIRE_EVENT, 500)

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(is_alt=True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        self.shooter = Shooter()
        self.shooter_group = pygame.sprite.Group(self.shooter)

    def start_game(self):
        print('start')

        while True:
            self.clock.tick(100)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == SHOOTER_FIRE_EVENT:
                self.shooter.fire()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_d]:
            self.shooter.speed = 6
        elif keys_pressed[pygame.K_a]:
            self.shooter.speed = -6
        else:
            self.shooter.speed = 0

    def __check_collide(self):
        pygame.sprite.groupcollide(self.shooter.bullets, self.enemy_group, True, True)
        enemies = pygame.sprite.spritecollide(self.shooter, self.enemy_group, True)

        if len(enemies) > 0:
            self.shooter.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.shooter_group.update()
        self.shooter_group.draw(self.screen)

        self.shooter.bullets.update()
        self.shooter.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print('Game Over')
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()

# shooter_rect = pygame.Rect(150, 300, 64, 64)
#
# enemy1 = GameSprite("blue-coronavirus.png")
# enemy2 = GameSprite('red-coronavirus.png', 2)
# enemy3 = GameSprite('green-coronavirus.png', 3)
# enemy_group = pygame.sprite.Group(enemy1, enemy2, enemy3)
