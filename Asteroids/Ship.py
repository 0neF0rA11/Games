from math import cos, sin, radians, atan
import random
import pygame


class Ship:

    def __init__(self, game_sc, size):
        self.__rects = []
        self.__game_sc = game_sc
        self.__angle = 0
        self.__alpha = 0
        self.__speed = 0
        self.__dx = 0
        self.__dy = 0
        self.__field = size
        self.__center = [size[0] / 2, size[1] / 2]
        self.__height, self.__width = 30, 20
        self.__coords = [[self.__center[0], self.__center[1] - self.__height / 2],
                         [self.__center[0] - self.__width / 2, self.__center[1] + self.__height / 2],
                         [self.__center[0] + self.__width / 2, self.__center[1] + self.__height / 2]]
        self.ship = pygame.draw.aalines(game_sc, pygame.Color("white"), True, self.__coords)

    def get_path(self):
        return self.__coords[0], self.__center

    def get_vectors(self):
        dx, dy = 0, 0
        if self.__center[0] == self.__coords[0][0]:
            dy = self.__speed if self.__center[0] < self.__coords[0][0] else -self.__speed
        elif self.__center[1] == self.__coords[0][1]:
            dx = self.__speed if self.__center[0] < self.__coords[0][0] else -self.__speed
        else:
            k = (self.__center[1] - self.__coords[0][1]) / (self.__center[0] - self.__coords[0][0])
            self.__alpha = atan(k)
            if self.__center[0] < self.__coords[0][0]:
                dx = self.__speed * cos(self.__alpha)
                dy = self.__speed * sin(self.__alpha)
            else:
                dx = -self.__speed * cos(self.__alpha)
                dy = -self.__speed * sin(self.__alpha)
        return dx, dy

    def move_turn(self, direction):
        self.__game_sc.fill((0, 0, 0), self.ship)
        self.__angle = (4 if direction else -4)
        for i in range(3):
            x = self.__coords[i][0] - self.__center[0]
            y = self.__coords[i][1] - self.__center[1]
            self.__coords[i][0] = x * cos(radians(self.__angle)) - y * sin(radians(self.__angle)) + self.__center[0]
            self.__coords[i][1] = x * sin(radians(self.__angle)) + y * cos(radians(self.__angle)) + self.__center[1]
        self.ship = pygame.draw.aalines(self.__game_sc, pygame.Color("white"), True, self.__coords)
        pygame.display.update(self.ship)

    def check_board(self, dx, dy):
        if self.__center[1] + dy > self.__field[1]:
            self.__center[1] -= self.__field[1]
            for i in range(3):
                self.__coords[i][1] -= self.__field[1]
        elif self.__center[1] + dy < 0:
            self.__center[1] += self.__field[1]
            for i in range(3):
                self.__coords[i][1] += self.__field[1]
        elif self.__center[0] + dx > self.__field[0]:
            self.__center[0] -= self.__field[0]
            for i in range(3):
                self.__coords[i][0] -= self.__field[0]
        elif self.__center[0] + dx < 0:
            self.__center[0] += self.__field[0]
            for i in range(3):
                self.__coords[i][0] += self.__field[0]
        else:
            self.__center[0] += dx
            self.__center[1] += dy
            for i in range(3):
                self.__coords[i][0] += dx
                self.__coords[i][1] += dy

    def ship_brake(self):
        for rect in self.__rects:
            self.__game_sc.fill((0, 0, 0), rect)
            self.__rects.remove(rect)
        self.__game_sc.fill((0, 0, 0), self.ship)
        if abs(self.__dx) > 0.05 or abs(self.__dy) > 0.05:
            self.__dx /= 1.02
            self.__dy /= 1.02
        else:
            self.__speed = 0
            self.__dx = 0
            self.__dy = 0
        self.check_board(self.__dx, self.__dy)
        self.ship = pygame.draw.aalines(self.__game_sc, pygame.Color("white"), True, self.__coords)
        pygame.display.update(self.ship)

    def speed_effect(self):
        for rect in self.__rects:
            self.__game_sc.fill((0, 0, 0), rect)

        self.__rects = [pygame.draw.rect(self.__game_sc, (255, 255, 255),
                                         (random.uniform(self.__coords[1][0], self.__coords[2][0]),
                                          random.uniform(self.__coords[1][1], self.__coords[2][1]),
                                          3, 3)) for i in range(5)]

    def move_forward(self):

        self.__game_sc.fill((0, 0, 0), self.ship)
        if self.__speed < 3:
            self.__speed += 0.2
        else:
            self.speed_effect()

        self.__dx, self.__dy = self.get_vectors()
        self.check_board(self.__dx, self.__dy)
        self.ship = pygame.draw.aalines(self.__game_sc, pygame.Color("white"), True, self.__coords)
        pygame.display.update(self.ship)

    def get_trigger(self):
        return self.__center, self.__height / 2
