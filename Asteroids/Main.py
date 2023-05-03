import pygame
from Board import Board
from Ship import Ship


class Main:

    def __init__(self):
        self.__FPS = 60

    def game(self):
        board = Board()
        game_sc, clock = board.create_board()
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            pygame.display.flip()
            clock.tick(self.__FPS)


Main().game()
