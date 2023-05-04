from math import cos, sin, radians, atan
import pygame


class Ship:

    def __init__(self, game_sc, size):
        self.__game_sc = game_sc
        self.__angle = 0
        self.__speed = 5
        self.__field = size
        self.__center = [size[0]/2, size[1]/2]
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

    def check_board(self, dx, dy):
        if self.__center[1] + dy > self.__field[1]:
            self.__center[1] = 0
            for i in range(3):
                self.__coords[i][1] -= self.__field[1]
        elif self.__center[1] + dy < 0:
            self.__center[1] = self.__field[1]
            for i in range(3):
                self.__coords[i][1] += self.__field[1]
        elif self.__center[0] + dx > self.__field[0]:
            self.__center[0] = 0
            for i in range(3):
                self.__coords[i][0] -= self.__field[0]
        elif self.__center[0] + dx < 0:
            self.__center[0] = self.__field[0]
            for i in range(3):
                self.__coords[i][0] += self.__field[0]
        else:
            self.__center[0] += dx
            self.__center[1] += dy
            for i in range(3):
                self.__coords[i][0] += dx
                self.__coords[i][1] += dy

    def ship_brake(self):
        pass

    def move_forward(self):
        self.__game_sc.fill((0, 0, 0), self.ship)

        if self.__center[0] == self.__coords[0][0]:
            dx = 0
            dy = self.__speed if self.__center[0] < self.__coords[0][0] else -self.__speed
        elif self.__center[1] == self.__coords[0][1]:
            dx = self.__speed if self.__center[0] < self.__coords[0][0] else -self.__speed
            dy = 0
        else:
            k = (self.__center[1]-self.__coords[0][1])/(self.__center[0]-self.__coords[0][0])
            alpha = atan(k)
            if self.__center[0] < self.__coords[0][0]:
                dx = self.__speed * cos(alpha)
                dy = self.__speed * sin(alpha)
            else:
                dx = -self.__speed * cos(alpha)
                dy = -self.__speed * sin(alpha)
        self.check_board(dx, dy)
        self.ship = pygame.draw.aalines(self.__game_sc, pygame.Color("white"), True, self.__coords)
        pygame.display.update(self.ship)

