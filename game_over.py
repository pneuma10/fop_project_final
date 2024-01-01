import pygame, sys
from fonts import *
from colors import *
from toolmodule import *
from spritesheets import *

# initialize pygame
pygame.init()


def over(screen, clock, running):

    width = screen.get_width() 
    height = screen.get_height() 

    ending_var = 0
    frame = 0
        
    
    while not running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        

        if ending_var >= 3:
            running = True

        if frame > 36:
            ending_var += 1
            frame = 0

            
        screen.fill(WHITE)

        loading_text = loading_font.render("Game Over", 1, green_of_text)
        screen.blit(loading_text, (width/2 - 175, 150))

        screen.blit(skull_img, (width/2 - 125, height/2 - 125))

        frame += 1
       

        # flip() updates the screen to make our changes visible
        pygame.display.flip()
        
        # how many updates per second
        clock.tick(20)
    

if __name__ == "__main__":

    ### DEFINE THE FOLLOWING IN THE MAIN MODULE
    screen_size = (1200, 800)
 
    # create a window
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("pygame Test")
    
    # clock is used to set a max fps
    clock = pygame.time.Clock()
    ###

    running = False

    over(screen, clock, running)

    pygame.quit()
 
