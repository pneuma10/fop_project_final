import pygame, sys
from fonts import *
from colors import *
from toolmodule import *
from spritesheets import *


# initialize pygame
pygame.init()


def won(screen, clock, running):

    width = screen.get_width() 
    height = screen.get_height() 

    ending_var = 0
    frame = 0
        
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        

        if ending_var == 5:
            running = False

        if frame > 36:
            ending_var += 1
            frame = 0

            
        screen.fill(WHITE)

        loading_text = loading_font.render("You Won", 1, green_of_text)
        screen.blit(loading_text, (width/2 - 125, 150))

        goldpot_frame = get_image(goldpot_spritesheet, frame, 500, 500, scale=0.5)
        screen.blit(goldpot_frame, (width/2 - 125, height/2 - 125))

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

    running = True

    won(screen, clock, running)

    pygame.quit()
 
