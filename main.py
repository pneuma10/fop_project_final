import pygame
from fonts import *
from colors import *
from you_won_screen import *
from game_over import *
from game_module import *
from menu import main_menu2



screen_size = (1200, 800)

# create a window
screen = pygame.display.set_mode(screen_size)

# clock is used to set a max fps
clock = pygame.time.Clock()


running = main_menu2(screen, clock)

# loadingscreen(screen, clock, running)
result = game(screen, screen_size, clock, running)

won(screen, clock, result)

over(screen, clock, result)



pygame.quit()