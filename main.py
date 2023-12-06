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
                game_init.screen.fill((0, 0, 0))
                game_init.init_sky_image_for_fullscreen()
                game_init.init_sun_image_fullscreen()
                game_init.draw_grid()
                game_init.world.draw()
                game_init.player.update()
                game_init.screen.blit(game_init.player.image, game_init.player.rect)
                pygame.display.update()
pygame.quit()
