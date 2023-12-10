# используемые библиотеки
import pygame
from pygame import mixer
import pickle
from os import path
import os


# используемые функции для инициализации игровых/интерфейсных элементов
def init_icon_game():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'avatar_for_game.bmp'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    avatarforgame = pygame.image.load(photo_path)
    return pygame.display.set_icon(avatarforgame)


def init_sky_image():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_sky.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    sky_img = pygame.image.load(photo_path)
    return sky_img


def init_sun_image():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_sun.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    sun_img = pygame.image.load(photo_path)
    return sun_img


def init_guy1():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_guy1.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_guy1 = pygame.image.load(photo_path)
    return icon_guy1


def init_guy2():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_guy2.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_guy2 = pygame.image.load(photo_path)
    return icon_guy2


def init_guy3():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_guy3.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_guy3 = pygame.image.load(photo_path)
    return icon_guy3


def init_guy4():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_guy4.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_guy4 = pygame.image.load(photo_path)
    return icon_guy4


def init_grass():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_grass.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_grass = pygame.image.load(photo_path)
    return icon_grass


def init_dirt():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_dirt.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_dirt = pygame.image.load(photo_path)
    return icon_dirt


def init_blob():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_blob.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_blob = pygame.image.load(photo_path)
    return icon_blob


def init_lava():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_lava.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_lava = pygame.image.load(photo_path)
    return icon_lava


def init_ghost():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_ghost.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_ghost = pygame.image.load(photo_path)
    return icon_ghost


def init_restart():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_restart.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_restart = pygame.image.load(photo_path)
    return icon_restart


def init_exit():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_exit.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_exit = pygame.image.load(photo_path)
    return icon_exit


def init_start():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_start.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_start = pygame.image.load(photo_path)
    return icon_start


def init_coin():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_coin.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_coin = pygame.image.load(photo_path)
    return icon_coin


def init_finish():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_finish.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_finish = pygame.image.load(photo_path)
    return icon_finish


def init_platform():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_platform.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_platform = pygame.image.load(photo_path)
    return icon_platform


def init_coin_sound():
    current_directory = os.path.dirname(__file__)
    images_folder = 'sounds'
    photo_filename = 'coin.wav'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    coin = pygame.mixer.Sound(photo_path)
    return coin


def init_gameover_sound():
    current_directory = os.path.dirname(__file__)
    images_folder = 'sounds'
    photo_filename = 'game_over.wav'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    gameover = pygame.mixer.Sound(photo_path)
    return gameover


def init_jump_sound():
    current_directory = os.path.dirname(__file__)
    images_folder = 'sounds'
    photo_filename = 'jump.wav'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    jump = pygame.mixer.Sound(photo_path)
    return jump


def init_music_sound():
    current_directory = os.path.dirname(__file__)
    images_folder = 'sounds'
    photo_filename = 'music.wav'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    MUS = pygame.mixer.music.load(photo_path)
    return MUS


pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

#  определяем фпс в игре
clock = pygame.time.Clock()
fps = 60
#  задаем базовое игровое разрешение
screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Прыжки это здорово!')
avatar_game = init_icon_game()

# определяем шрифт
font = pygame.font.SysFont('Bauhaus 93', 70)
font_score = pygame.font.SysFont('Bauhaus 93', 30)

# различные игровые переменные для функционирования игры
tile_size = 50
game_over = 0
main_menu = True
level = 3
max_levels = 7
score = 0

# основные цвета
white = (255, 255, 255)
blue = (0, 0, 255)

# подгрузка фотографий
sun_img = init_sun_image()
bg_img = init_sky_image()
restart_img = init_restart()
start_img = init_start()
exit_img = init_exit()

# подгрузка звуков и музыки
mus = init_music_sound()
pygame.mixer.music.play(-1, 0.0, 5000)
coin_fx = init_coin_sound()
coin_fx.set_volume(0.5)
jump_fx = init_jump_sound()
jump_fx.set_volume(0.5)
game_over_fx = init_gameover_sound()
game_over_fx.set_volume(0.5)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# определение функции для рестарта уровня
def reset_level(level):
    player.reset(100, screen_height - 130)
    blob_group.empty()
    platform_group.empty()
    coin_group.empty()
    lava_group.empty()
    exit_group.empty()

    # подгружаем игровые уровни и создаем игровой мир
    if path.exists(f'level{level}_data'):
        pickle_in = open(f'level{level}_data', 'rb')
        world_data = pickle.load(pickle_in)
    world = World(world_data)
    # create dummy coin for showing the score
    score_coin = Coin(tile_size // 2, tile_size // 2)
    coin_group.add(score_coin)
    return world


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button
        screen.blit(self.image, self.rect)

        return action


class Player():
    def __init__(self, x, y):
        self.reset(x, y)

    def update(self, game_over):
        dx = 0
        dy = 0
        walk_cooldown = 5
        col_thresh = 20

        if game_over == 0:
            # get keypresses
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False and not self.in_air:
                jump_fx.play()
                self.vel_y = -15
                self.jumped = True
            if not key[pygame.K_SPACE]:
                self.jumped = False
            if key[pygame.K_LEFT]:
                dx -= 5
                self.counter += 1
                self.direction = -1
            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1
            if key[pygame.K_LEFT] == False and not key[pygame.K_RIGHT]:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # handle animation
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            # check for collision
            self.in_air = True
            for tile in world.tile_list:
                # check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                # check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # check if above the ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            # check for collision with enemies
            if pygame.sprite.spritecollide(self, blob_group, False):
                game_over = -1
                game_over_fx.play()

            # check for collision with lava
            if pygame.sprite.spritecollide(self, lava_group, False):
                game_over = -1
                game_over_fx.play()

            # check for collision with exit
            if pygame.sprite.spritecollide(self, exit_group, False):
                game_over = 1

            # check for collision with platforms
            for platform in platform_group:
                # collision in the x direction
                if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                # collision in the y direction
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # check if below platform
                    if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
                        self.vel_y = 0
                        dy = platform.rect.bottom - self.rect.top
                    # check if above platform
                    elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
                        self.rect.bottom = platform.rect.top - 1
                        self.in_air = False
                        dy = 0
                    # move sideways with the platform
                    if platform.move_x != 0:
                        self.rect.x += platform.move_direction

            # update player coordinates
            self.rect.x += dx
            self.rect.y += dy


        elif game_over == -1:
            self.image = self.dead_image
            draw_text('GAME OVER!', font, blue, (screen_width // 2) - 200, screen_height // 2)
            if self.rect.y > 200:
                self.rect.y -= 5

        # draw player onto screen
        screen.blit(self.image, self.rect)

        return game_over

    def reset(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = globals()[f'init_guy{num}']()
            img_right = pygame.transform.scale(img_right, (40, 80))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.dead_image = init_ghost()
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True


class World():
    def __init__(self, data):
        self.tile_list = []

        # load images
        dirt_img = init_dirt()
        grass_img = init_grass()

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    blob = Enemy(col_count * tile_size, row_count * tile_size + 15)
                    blob_group.add(blob)
                if tile == 4:
                    platform = Platform(col_count * tile_size, row_count * tile_size, 1, 0)
                    platform_group.add(platform)
                if tile == 5:
                    platform = Platform(col_count * tile_size, row_count * tile_size, 0, 1)
                    platform_group.add(platform)
                if tile == 6:
                    lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size // 2))
                    lava_group.add(lava)
                if tile == 7:
                    coin = Coin(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
                    coin_group.add(coin)
                if tile == 8:
                    finish = Finish(col_count * tile_size, row_count * tile_size - (tile_size // 2))
                    exit_group.add(finish)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = init_blob()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, move_x, move_y):
        pygame.sprite.Sprite.__init__(self)
        img = init_platform()
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.move_direction = 1
        self.move_x = move_x
        self.move_y = move_y

    def update(self):
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction * self.move_y
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1


class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = init_lava()
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = init_coin()
        self.image = pygame.transform.scale(img, (tile_size // 2, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class Finish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = init_finish()
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


player = Player(100, screen_height - 130)

blob_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()

# create dummy coin for showing the score
score_coin = Coin(tile_size // 2, tile_size // 2)
coin_group.add(score_coin)

# load in level data and create world
if path.exists(f'level{level}_data'):
    pickle_in = open(f'level{level}_data', 'rb')
    world_data = pickle.load(pickle_in)
world = World(world_data)

# create buttons
restart_button = Button(screen_width // 2 - 50, screen_height // 2 + 100, restart_img)
start_button = Button(screen_width // 2 - 350, screen_height // 2, start_img)
exit_button = Button(screen_width // 2 + 150, screen_height // 2, exit_img)

run = True
while run:

    clock.tick(fps)

    screen.blit(bg_img, (0, 0))
    screen.blit(sun_img, (100, 100))

    if main_menu:
        if exit_button.draw():
            run = False
        if start_button.draw():
            main_menu = False
    else:
        world.draw()

        if game_over == 0:
            blob_group.update()
            platform_group.update()
            # update score
            # check if a coin has been collected
            if pygame.sprite.spritecollide(player, coin_group, True):
                score += 1
                coin_fx.play()
            draw_text('X ' + str(score), font_score, white, tile_size - 10, 10)

        blob_group.draw(screen)
        platform_group.draw(screen)
        lava_group.draw(screen)
        coin_group.draw(screen)
        exit_group.draw(screen)

        game_over = player.update(game_over)

        # если игрок умер, то нужно перезагрузить текущий уровень
        if game_over == -1:
            if restart_button.draw():
                world_data = []
                world = reset_level(level)
                game_over = 0
                score = 0

        # если игрок прошёл текущий уровень
        if game_over == 1:
            # то идём на следующий уровень
            level += 1
            if level <= max_levels:
                # если уровни пройдены, то игра окончена
                world_data = []
                world = reset_level(level)
                game_over = 0
            else:
                draw_text('YOU WIN!', font, blue, (screen_width // 2) - 140, screen_height // 2)
                if restart_button.draw():
                    level = 1
                    # reset level
                    world_data = []
                    world = reset_level(level)
                    game_over = 0
                    score = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
