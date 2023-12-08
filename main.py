from game_initial import game_init
import pygame

game_init.init_window()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                game_init.change_the_screen()
            if event.key == pygame.K_LEFT:
                game_init.press_K_LEFT()
            if event.key == pygame.K_SPACE:
                game_init.press_K_SPACE()
            if event.key == pygame.K_RIGHT:
                game_init.press_K_RIGHT()
        pygame.display.update()
pygame.quit()
#globals()[f'init_guy{num}']()