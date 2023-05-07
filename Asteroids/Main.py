import pygame
from Board import Board
from Ship import Ship
import time


class Main:

    def __init__(self):
        self.__FPS = 60

    def game(self):
        board = Board()
        game_sc, clock = board.create_board()
        ship = Ship(game_sc, board.get_size())
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            keys = pygame.key.get_pressed()
            if (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]) and keys[pygame.K_UP]:
                if keys[pygame.K_RIGHT]:
                    ship.move_turn(True)
                else:
                    ship.move_turn(False)
                ship.move_forward()
                clock.tick(self.__FPS * 4)
            elif keys[pygame.K_RIGHT]:
                ship.ship_brake()
                ship.move_turn(True)
                clock.tick(self.__FPS*4)
            elif keys[pygame.K_LEFT]:
                ship.ship_brake()
                ship.move_turn(False)
                clock.tick(self.__FPS*4)
            elif keys[pygame.K_UP]:
                ship.move_forward()
                clock.tick(self.__FPS*4)
            elif not keys[pygame.K_UP]:
                ship.ship_brake()
                clock.tick(self.__FPS)

            pygame.display.flip()
            clock.tick(self.__FPS)


Main().game()
