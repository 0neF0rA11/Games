from  math import cos, sin, radians, asin
import pygame


class Ship:

    def __init__(self, game_sc, size):
        self.__game_sc = game_sc
        self.__angle = 0
        self.__center = (size[0]/2, size[1]/2)
        self.__height, self.__width = 30, 20
        self.__coords = [[self.__center[0],  self.__center[1]-self.__height/2],
                         [self.__center[0]-self.__width/2,  self.__center[1]+self.__height/2],
                         [self.__center[0]+self.__width/2,  self.__center[1]+self.__height/2]]
        self.ship = pygame.draw.aalines(game_sc, pygame.Color("white"), True, self.__coords)

    def move_turn(self, direction):
        self.__game_sc.fill((0, 0, 0), self.ship)
        self.__angle = (5 if direction else -5)
        for i in range(3):
            x = self.__coords[i][0] - self.__center[0]
            y = self.__coords[i][1] - self.__center[1]
            self.__coords[i][0] = x * cos(radians(self.__angle)) - y * sin(radians(self.__angle)) + self.__center[0]
            self.__coords[i][1] = x * sin(radians(self.__angle)) + y * cos(radians(self.__angle)) + self.__center[1]
        self.ship = pygame.draw.aalines(self.__game_sc, pygame.Color("white"), True, self.__coords)

        pygame.display.update(self.ship)
