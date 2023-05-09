import pygame
from math import sin, cos, atan


class Rocket:

    def __init__(self, game_sc, size, coords):
        self.__game_sc = game_sc
        self.__field = size
        self.__center = coords[0].copy()
        self.__time_point = coords[1]
        self.__rocket_r = 8
        self.__speed = 10
        self.__dx, self.__dy = self.get_vector(self.__center, self.__time_point)
        self.rocket = pygame.draw.circle(game_sc, pygame.Color("red"), self.__center, self.__rocket_r)

    def start(self):
        self.__game_sc.fill((0, 0, 0), self.rocket)
        if not self.__check_board(self.__dx, self.__dy):
            self.rocket = pygame.draw.circle(self.__game_sc, pygame.Color("red"), self.__center, self.__rocket_r)
            pygame.display.update(self.rocket)
        else:
            pygame.display.update(self.rocket)
            return True

    def __check_board(self, dx, dy):
        if (self.__center[1] + dy > self.__field[1]) or (self.__center[1] + dy < 0) or \
                (self.__center[0] + dx > self.__field[0]) or (self.__center[0] + dx < 0):
            return True
        else:
            self.__center[0] += dx
            self.__center[1] += dy
            return False

    def get_vector(self, point_front, point_back):
        dx, dy = 0, 0
        if point_back[0] == point_front[0]:
            dy = self.__speed if point_back[0] < point_front[0] else -self.__speed
        elif point_back[1] == point_front[1]:
            dx = self.__speed if point_back[0] < point_front[0] else -self.__speed
        else:
            k = (point_back[1] - point_front[1]) / (point_back[0] - point_front[0])
            alpha = atan(k)
            if point_back[0] < point_front[0]:
                dx = self.__speed * cos(alpha)
                dy = self.__speed * sin(alpha)
            else:
                dx = -self.__speed * cos(alpha)
                dy = -self.__speed * sin(alpha)
        return dx, dy
