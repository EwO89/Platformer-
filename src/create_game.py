import pygame
import pickle
from os import path

pygame.init()

clock = pygame.time.Clock()
fps = 60

# Игровое окно
tile_size = 50
cols = 20
margin = 100
screen_width = tile_size * cols
screen_height = (tile_size * cols) + margin

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Редактор уровней')

# Загрузка изображений
sun_img = pygame.image.load('img/sun.png')
sun_img = pygame.transform.scale(sun_img, (tile_size, tile_size))
bg_img = pygame.image.load('img/sky.png')
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height - margin))
dirt_img = pygame.image.load('img/dirt.png')
grass_img = pygame.image.load('img/grass.png')
blob_img = pygame.image.load('img/blob.png')
platform_x_img = pygame.image.load('img/platform_x.png')
platform_y_img = pygame.image.load('img/platform_y.png')
lava_img = pygame.image.load('img/lava.png')
coin_img = pygame.image.load('img/coin.png')
exit_img = pygame.image.load('img/exit.png')
save_img = pygame.image.load('img/save_btn.png')
load_img = pygame.image.load('img/load_btn.png')

# Определение игровых переменных
clicked = False
level = 1

# Определение цветов
white = (255, 255, 255)
green = (144, 201, 120)

font = pygame.font.SysFont('Futura', 24)

# Создание пустого списка для тайлов
world_data = []
for row in range(20):
    r = [0] * 20
    world_data.append(r)

# Создание границы
for tile in range(0, 20):
    world_data[19][tile] = 2
    world_data[0][tile] = 1
    world_data[tile][0] = 1
    world_data[tile][19] = 1

# Функция для вывода текста на экран
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Функция для рисования сетки
def draw_grid():
    for c in range(21):
        # Вертикальные линии
        pygame.draw.line(screen, white, (c * tile_size, 0), (c * tile_size, screen_height - margin))
        # Горизонтальные линии
        pygame.draw.line(screen, white, (0, c * tile_size), (screen_width, c * tile_size))

# Функция для рисования мира
def draw_world():
    for row in range(20):
        for col in range(20):
            if world_data[row][col] > 0:
                if world_data[row][col] == 1:
                    # Блоки земли
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 2:
                    # Блоки травы
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 3:
                    # Блоки врагов
                    img = pygame.transform.scale(blob_img, (tile_size, int(tile_size * 0.75)))
                    screen.blit(img, (col * tile_size, row * tile_size + (tile_size * 0.25)))
                if world_data[row][col] == 4:
                    # Горизонтально движущиеся платформы
                    img = pygame.transform.scale(platform_x_img, (tile_size, tile_size // 2))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 5:
                    # Вертикально движущиеся платформы
                    img = pygame.transform.scale(platform_y_img, (tile_size, tile_size // 2))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 6:
                    # Лава
                    img = pygame.transform.scale(lava_img, (tile_size, tile_size // 2))
                    screen.blit(img, (col * tile_size, row * tile_size + (tile_size // 2)))
                if world_data[row][col] == 7:
                    # Монеты
                    img = pygame.transform.scale(coin_img, (tile_size // 2, tile_size // 2))
                    screen.blit(img, (col * tile_size + (tile_size // 4), row * tile_size + (tile_size // 4)))
                if world_data[row][col] == 8:
                    # Выход
                    img = pygame.transform.scale(exit_img, (tile_size, int(tile_size * 1.5)))
                    screen.blit(img, (col * tile_size, row * tile_size - (tile_size // 2)))

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        # Получение позиции мыши
        pos = pygame.mouse.get_pos()

        # Проверка условий наведения и клика
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Отрисовка кнопки
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

# Создание кнопок загрузки и сохранения
save_button = Button(screen_width // 2 - 150, screen_height - 80, save_img)
load_button = Button(screen_width // 2 + 50, screen_height - 80, load_img)

# Главный игровой цикл
run = True
while run:

    clock.tick(fps)

    # Рисуем фон
    screen.fill(green)
    screen.blit(bg_img, (0, 0))
    screen.blit(sun_img, (tile_size * 2, tile_size * 2))

    # Загрузка и сохранение уровня
    if save_button.draw():
        # Сохранение данных уровня
        pickle_out = open(f'level{level}_data', 'wb')
        pickle.dump(world_data, pickle_out)
        pickle_out.close()
    if load_button.draw():
        # Загрузка данных уровня
        if path.exists(f'level{level}_data'):
            pickle_in = open(f'level{level}_data', 'rb')
            world_data = pickle.load(pickle_in)

    # Показ сетки и отрисовка тайлов уровня
    draw_grid()
    draw_world()

    # Текст, показывающий текущий уровень
    draw_text(f'Уровень: {level}', font, white, tile_size, screen_height - 60)
    draw_text('Нажмите ВВЕРХ или ВНИЗ для смены уровня', font, white, tile_size, screen_height - 40)

    # Обработка событий
    for event in pygame.event.get():
        # Выход из игры
        if event.type == pygame.QUIT:
            run = False
        # Клики мыши для изменения тайлов
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
            pos = pygame.mouse.get_pos()
            x = pos[0] // tile_size
            y = pos[1] // tile_size
            # Проверка, что координаты находятся в области тайлов
            if x < 20 and y < 20:
                # Обновление значения тайла
                if pygame.mouse.get_pressed()[0] == 1:
                    world_data[y][x] += 1
                    if world_data[y][x] > 8:
                        world_data[y][x] = 0
                elif pygame.mouse.get_pressed()[2] == 1:
                    world_data[y][x] -= 1
                    if world_data[y][x] < 0:
                        world_data[y][x] = 8
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
        # Нажатия клавиш ВВЕРХ и ВНИЗ для смены номера уровня
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                level += 1
            elif event.key == pygame.K_DOWN and level > 1:
                level -= 1

    # Обновление игрового окна
    pygame.display.update()

pygame.quit()
