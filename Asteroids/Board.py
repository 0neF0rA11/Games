import pygame


class Board:

    def __init__(self):
        self.__HIGH = 600
        self.__WIDE = 800

    def get_size(self):
        return self.__WIDE, self.__HIGH

    def create_board(self):
        pygame.init()
        game_sc = pygame.display.set_mode((self.__WIDE, self.__HIGH))
        game_sc.fill(pygame.Color('black'))
        clock = pygame.time.Clock()
        return game_sc, clock
