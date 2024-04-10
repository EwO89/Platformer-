import pygame
import os
import sys
import pytest
# Добавляем путь к игре в sys.path, чтобы иметь возможность импортировать модули игры

sys.path.append('C:\Platformer-\src')

# Теперь мы можем импортировать модули игры.
from src.main import *  # Импортируем основной скрипт игры



# Для начала напишем тест, который проверяет инициализацию pygame и загрузку ресурсов.
def test_pygame_initialization():
    pygame.init()
    assert pygame.get_init() == True, "Pygame не был инициализирован"


def test_images_load():
    """
    Тест загрузки изображений.
    Этот тест будет проверять, правильно ли загружаются изображения.
    """
    try:
        sun_img = pygame.image.load('images/sun.png')
        bg_img = pygame.image.load('images/sky.png')
        dirt_img = pygame.image.load('images/dirt.png')
        # Продолжаем загрузку остальных изображений...
    except pygame.error as e:
        assert False, f"Не удалось загрузить изображения: {e}"


def test_sounds_load():
    """
    Тест загрузки звуков.
    Этот тест будет проверять, правильно ли загружаются звуки.
    """
    try:
        coin_sound = pygame.mixer.Sound('sounds/coin.wav')
        jump_sound = pygame.mixer.Sound('sounds/jump.wav')

    except pygame.error as e:
        assert False, f"Не удалось загрузить звуки: {e}"



def test_level_data_load():
    """
    Тест загрузки данных уровня.
    Этот тест будет проверять, правильно ли загружаются данные уровней.
    """
    level = 1
    try:
        with open(f'level{level}_data', 'rb') as f:
            level_data = pickle.load(f)
        assert isinstance(level_data, list), "Данные уровня не являются списком"
        assert len(level_data) > 0, "Список данных уровня пуст"
    except Exception as e:
        assert False, f"Ошибка при загрузке данных уровня: {e}"


