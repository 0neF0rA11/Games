import pygame
from Board import Board
from Ship import Ship
from Rocket import Rocket
from Asteroid import Asteroid


class Main:

    def __init__(self):
        self.__FPS = 60
        self.lives = 3
        self.score = 0

    def detonate(self, object1, object2):
        distance = ((object1[0][0] - object2[0][0])**2 + (object1[0][1] - object2[0][1])**2)**(1/2)
        if distance <= object1[1]+object2[1]:
            return True
        return False

    def game(self):
        board = Board()
        game_sc, clock = board.create_board()
        ship = Ship(game_sc, board.get_size())
        rockets = []
        time_create = pygame.time.get_ticks()
        asteroids_list = [Asteroid(game_sc, board.get_size())]
        while True:

            if pygame.time.get_ticks() - time_create >= 3000 or len(asteroids_list) == 0:
                time_create = pygame.time.get_ticks()
                asteroids_list.append(Asteroid(game_sc, board.get_size()))

            for asteroid in asteroids_list:
                asteroid.move()

            for asteroid in asteroids_list:
                if self.detonate(ship.get_trigger(), asteroid.get_trigger()):
                    self.lives -= 1
                    asteroid.kill()
                    asteroids_list.remove(asteroid)
                    continue
                for rocket in rockets:
                    if self.detonate(rocket.get_trigger(), asteroid.get_trigger()):
                        self.score += 500
                        asteroid.kill()
                        asteroids_list.remove(asteroid)
                        rocket.kill()
                        rockets.remove(rocket)
                        break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        rockets.append(Rocket(game_sc, board.get_size(), ship.get_path()))

            keys = pygame.key.get_pressed()
            if (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]) and keys[pygame.K_UP]:
                if keys[pygame.K_RIGHT]:
                    ship.move_turn(True)
                else:
                    ship.move_turn(False)
                ship.move_forward()
            elif keys[pygame.K_RIGHT]:
                ship.ship_brake()
                ship.move_turn(True)
            elif keys[pygame.K_LEFT]:
                ship.ship_brake()
                ship.move_turn(False)
            elif keys[pygame.K_UP]:
                ship.move_forward()
            elif not keys[pygame.K_UP]:
                ship.ship_brake()

            for rocket in rockets:
                if rocket.start():
                    rockets.remove(rocket)

            pygame.display.flip()
            clock.tick(self.__FPS)


Main().game()
