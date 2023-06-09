import pygame
import random
from math import sin, cos, atan


class Asteroid:

    def __init__(self, game_sc, size):
        self.__game_sc = game_sc
        self.__field = size
        self.__angle = 0
        self.__angle_speed = random.randint(1, 20)
        self.__speed = random.randint(1, 4)
        self.__center = [random.randint(0, 800), random.randint(0, 600)]
        self.__time_point = (random.randint(1, 800), random.randint(1, 600))
        self.__dx, self.__dy = self.__get_vector(self.__time_point, self.__center)
        self.i = 1

        self.__img = pygame.image.load(f'pictures/Asteroid{random.randint(1, 2)}.png').convert_alpha()
        self.__rect = self.__img.get_bounding_rect()
        self.__rect.center = self.__center
        self.asteroid = self.__game_sc.blit(self.__img, self.__rect)

    def move(self):
        self.__game_sc.fill((0, 0, 0), self.asteroid)
        self.__game_sc.set_colorkey((0, 0, 0))
        self.__angle += self.__angle_speed
        rotated_img = pygame.transform.rotate(self.__img, self.__angle).convert_alpha()
        self.__rect = rotated_img.get_rect()

        self.__check_board(self.__dx, self.__dy)
        self.__rect.center = self.__center

        self.asteroid = self.__game_sc.blit(rotated_img, self.__rect)
        pygame.display.update(self.asteroid)

    def __get_vector(self, point_front, point_back):
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

    def __check_board(self, dx, dy):
        if self.__center[1] + dy > self.__field[1]:
            self.__center[1] -= self.__field[1]
        elif self.__center[1] + dy < 0:
            self.__center[1] += self.__field[1]
        elif self.__center[0] + dx > self.__field[0]:
            self.__center[0] -= self.__field[0]
        elif self.__center[0] + dx < 0:
            self.__center[0] += self.__field[0]
        else:
            self.__center[0] += dx
            self.__center[1] += dy

    def get_trigger(self):
        return self.__center, max(self.__rect.size)//2

    def explosion(self):
        self.__game_sc.fill((0, 0, 0), self.asteroid)
        filename = f"pictures/bang/bang_{self.i}.png"
        img = pygame.image.load(filename)
        scaled_img = pygame.transform.scale(img, (102, 100))
        scaled_img.set_colorkey((69, 86, 106))
        self.asteroid = self.__game_sc.blit(scaled_img, (self.__center[0]-50, self.__center[1]-50))
        self.i += 1
        if self.i == 9:
            self.kill()

    def kill(self):
        self.__game_sc.fill((0, 0, 0), self.asteroid)
