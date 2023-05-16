import pygame
from Board import Board
from Ship import Ship
from Rocket import Rocket
from Asteroid import Asteroid
from LoadScreen import LoadScreen


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

    def start(self):
        main_menu = LoadScreen().main_menu()
        if main_menu:
            return self.game()

    def game(self):
        pygame.mixer.music.stop()

        background_music = pygame.mixer.Sound('sounds/play.mp3')
        shot_music = pygame.mixer.Sound('sounds/shot.mp3')
        blast_music = pygame.mixer.Sound('sounds/blast.mp3')
        game_over_music = pygame.mixer.Sound('sounds/game_over.mp3')
        hit_music = pygame.mixer.Sound('sounds/hit.mp3')
        channel1 = pygame.mixer.Channel(0)
        channel2 = pygame.mixer.Channel(1)
        channel3 = pygame.mixer.Channel(2)
        channel4 = pygame.mixer.Channel(3)
        channel1.play(background_music, loops=-1)

        board = Board()
        game_sc, clock = board.create_board()

        font = pygame.font.Font("fonts/toony_loons.ttf.otf", 35)
        score = font.render(f'Score: {self.score}', True, (255, 255, 255))
        game_sc.blit(score, (600, 20))

        heart = pygame.image.load("pictures/heart.png")
        edge_heart = [10, 20]

        ship = Ship(game_sc, board.get_size())
        rockets = []
        time_create = pygame.time.get_ticks()
        asteroids_list = [Asteroid(game_sc, board.get_size())]
        destroy_aster = []
        while True:
            pygame.draw.rect(game_sc, (0, 0, 0), pygame.Rect(600, 20, 200, 34))
            pygame.draw.rect(game_sc, (0, 0, 0), pygame.Rect(edge_heart[0], edge_heart[1], 170, 37))

            if pygame.time.get_ticks() - time_create >= 3000 or len(asteroids_list) == 0:
                time_create = pygame.time.get_ticks()
                asteroids_list.append(Asteroid(game_sc, board.get_size()))

            for asteroid in destroy_aster:
                asteroid.explosion()
                if asteroid.i == 9:
                    destroy_aster.remove(asteroid)

            for asteroid in asteroids_list:
                asteroid.move()

            for asteroid in asteroids_list:
                if self.detonate(ship.get_trigger(), asteroid.get_trigger()):
                    self.lives -= 1
                    if self.lives == 0:
                        self.lives = 3
                        self.score = 0
                        channel1.play(game_over_music)
                        self.start()
                    asteroid.kill()
                    channel4.play(hit_music)
                    destroy_aster.append(asteroid)
                    asteroids_list.remove(asteroid)
                    continue
                for rocket in rockets:
                    if self.detonate(rocket.get_trigger(), asteroid.get_trigger()):
                        self.score += 500
                        rocket.kill()
                        rockets.remove(rocket)
                        asteroid.kill()
                        channel3.play(blast_music)
                        destroy_aster.append(asteroid)
                        asteroids_list.remove(asteroid)
                        break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        rockets.append(Rocket(game_sc, board.get_size(), ship.get_path()))
                        channel2.play(shot_music)

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

            score = font.render(f'Score: {self.score}', True, (255, 255, 255))
            game_sc.blit(score, (600, 20))

            for i in range(self.lives):
                if self.lives == 1:
                    edge_heart[0] = 5 if edge_heart[0] != 5 else 10
                game_sc.blit(heart, (edge_heart[0]+60*i, edge_heart[1]))

            pygame.display.flip()
            clock.tick(self.__FPS)


Main().start()
