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


def init_finish():
    current_directory = os.path.dirname(__file__)
    images_folder = 'images'
    photo_filename = 'icon_finish.png'
    photo_path = os.path.join(current_directory, images_folder, photo_filename)
    icon_finish = pygame.image.load(photo_path)
    return icon_finish


sun_img = init_sun_image()
bg_img = init_sky_image()
restart_img = init_restart()
start_img = init_start()
exit_img = init_exit()