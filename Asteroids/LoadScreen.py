import pygame
from Board import Board
from Ship import Ship


class LoadScreen:

    def __init__(self):
        self.__FPS = 60

    def main_menu(self):
        board = Board()
        game_sc, clock = board.create_board()
        Ship(game_sc, board.get_size())
        pygame.mixer.music.load('sounds/menu.mp3')
        pygame.mixer.music.play(-1)
        font = pygame.font.Font("fonts/Donpoligrafbum-Bold.otf", 36)
        font_button = pygame.font.Font("fonts/toony_loons.ttf.otf", 30)
        text_surface = font.render('Asteroids', True, (127, 132, 123))
        game_sc.blit(text_surface, (200, 150))
        play = font_button.render('Погнали', True, (232, 162, 54))
        game_sc.blit(play, (355, 350))
        quit = font_button.render('Выход', True, (232, 162, 54))
        game_sc.blit(quit, (363, 400))
        pygame.display.update()
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            mouse_pos = pygame.mouse.get_pos()
            is_clicked = pygame.mouse.get_pressed()[0]
            if 350 <= mouse_pos[0] <= 450 and 350 <= mouse_pos[1] <= 380 and is_clicked:
                return True
            elif 361 <= mouse_pos[0] <= 444 and 400 <= mouse_pos[1] <= 427 and is_clicked:
                exit()

            pygame.display.flip()
            clock.tick(self.__FPS)

