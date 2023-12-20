import pygame
import os


def init_icon_image():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'avatar_for_game.bmp'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_game = pygame.image.load(photo_path)
    return pygame.display.set_icon(icon_game)


def init_window():
    init_screen()
    init_icon_image()
    init_name_game()
    #fps_limit()
    init_sky_image_for_fullscreen()
    init_sun_image_fullscreen()
    draw_grid()
    player.update()
    screen.blit(player.image, player.rect)
    world.draw()


name_game = None


def init_name_game():
    global name_game
    name_game = 'Прыжки это здорово'
    return pygame.display.set_caption(name_game)


width, height = None, None


def init_screen():
    pygame.init()
    global width, height
    width, height = 1000, 1000
    global screen
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
    return screen


screen = None


def init_sun_image_fullscreen():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_sun.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_sun = pygame.image.load(photo_path)
    width, height = 100, 100
    screen.blit(icon_sun, (width, height))


def init_sun_image_frame_screen():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_sun.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_sun = pygame.image.load(photo_path)
    new_width_for_frame_screen, new_height_for_frame_screen = screen.get_width() // 10, screen.get_height() // 10
    scaled_icon_sun = pygame.transform.scale(icon_sun, (new_width_for_frame_screen, new_height_for_frame_screen))
    screen.blit(scaled_icon_sun, (100, 100))


def init_sky_image_for_fullscreen():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_sky.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_sky = pygame.image.load(photo_path)
    width, height = 0, 0
    screen.blit(icon_sky, (width, height))


def change_the_screen():
    is_fullscreen = screen.get_flags() & pygame.FULLSCREEN != 0
    if is_fullscreen:
        width, height = 1000, 1000
        pygame.display.set_mode((width, height), pygame.RESIZABLE | pygame.DOUBLEBUF)
        init_sky_image_for_fullscreen()
        init_sun_image_frame_screen()
        draw_grid()
    else:
        width, height = 1000, 1000
        pygame.display.set_mode((width, height), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
        init_sky_image_for_fullscreen()
        init_sun_image_fullscreen()
        draw_grid()


'''def fps_limit():
    clock = pygame.time.Clock()
    fps = 60
    clock.tick(fps)'''


tile_size = 50


def show_tile_size():
    return tile_size


def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, height))


def init_dirt():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_dirt.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_dirt = pygame.image.load(photo_path)
    return icon_dirt


def init_grass():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_grass.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_grass = pygame.image.load(photo_path)
    return icon_grass


def show_screen():
    return screen


def init_guy1():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_guy1.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_guy1 = pygame.image.load(photo_path)
    return icon_guy1


class World:
    def __init__(self, data):
        self.tile_list = []
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(init_dirt(), (show_tile_size(), show_tile_size()))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * show_tile_size()
                    img_rect.y = row_count * show_tile_size()
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(init_grass(), (show_tile_size(), show_tile_size()))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * show_tile_size()
                    img_rect.y = row_count * show_tile_size()
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(init_guy1(), (40, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False

    def update(self):
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and not self.jumped:
            self.vel_y = -15
            self.jumped = True
        if not key[pygame.K_SPACE]:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 5
        if key[pygame.K_RIGHT]:
            dx += 5
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y


        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > height:
            self.rect.bottom = height
            dy = 0


world_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
    [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
    [1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
player = Player(100, 1000 - 130)
world = World(world_data)


def press_K_SPACE():
    screen.fill((0, 0, 0))
    init_sky_image_for_fullscreen()
    init_sun_image_fullscreen()
    draw_grid()
    player.update()
    world.draw()
    screen.blit(player.image, player.rect)


def press_K_RIGHT():
    screen.fill((0, 0, 0))
    init_sky_image_for_fullscreen()
    init_sun_image_fullscreen()
    draw_grid()
    player.update()
    world.draw()
    screen.blit(player.image, player.rect)


def press_K_LEFT():
    screen.fill((0, 0, 0))
    init_sky_image_for_fullscreen()
    init_sun_image_fullscreen()
    draw_grid()
    player.update()
    world.draw()
    screen.blit(player.image, player.rect)
