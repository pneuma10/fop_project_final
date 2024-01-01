import pygame, sys
from toolmodule import *
from colors import *
from spritesheets import *
from framesforgameplay import *


# initialize pygame
pygame.init()


def game(screen, screen_size, clock, running):
 
    K_RIGHT = 1073741903
    K_LEFT = 1073741904
    K_UP = 1073741906
    K_DOWN = 1073741905
    K_Z = 122

    # variables for animations
    frame, frame2, frame3, pl1, pl3, ground_pos_x = 0, 0, 0, 0, 0, 0


    player_health = 400


    moveRight, moveLeft, moveRight, moveDown, fight = False, False, False, False, False

  

    ### MAIN CHARACTER GOBLIN
    goblin_idle_frame = goblin_frames(0, 0, 0)[3]
    goblin_THE_frame = goblin_idle_frame
    goblin_main_rect = goblin_THE_frame.get_rect(midbottom = (100, 697))

   

    # GOLD POT END
    gold_pot = golden_pot()
    gold_pot_rect = gold_pot.get_rect(midbottom = (3800, 613))

    while running:

        # Get the variables back to zero for the animation
        if frame > 7:
            frame = 0
        if frame2 > 3:
            frame2 = 0 
        if pl1 > 149:
            pl1 = 0
        if pl3 > 80:
            pl3 = 0

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                sys.exit()

            ### KEYEVENTS
            if event.type == pygame.KEYDOWN:
                # Change the keyboard variables.
                print(event.key)
                if event.key == K_LEFT:
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT:
                    moveLeft = False
                    moveRight = True
                if event.key == K_Z:
                    fight = True
            if event.type == pygame.KEYUP:
                if event.key == K_LEFT:
                    moveLeft = False
                if event.key == K_RIGHT:
                    moveRight = False
                if event.key == K_Z:
                    fight = False
            else:
                pass


        if fight:
            if moveRight:
                goblin_main_rect.x += 3
            if moveLeft:
                goblin_main_rect.x -= 3
            goblin_THE_frame = goblin_attack_frame  


          
        elif moveRight:

            if goblin_main_rect.x < 200 or gold_pot_rect.x <= 1050:
                goblin_main_rect.x += 10



            if gold_pot_rect.x > 1050:
                gold_pot_rect.x -= 10

                if not goblin_main_rect.x < 200:
                    ground_pos_x -= 10



            goblin_THE_frame = goblin_run_frame

        elif moveLeft:
            goblin_THE_frame = goblin_run_frame
            goblin_main_rect.x -= 10


        else:
            goblin_THE_frame = goblin_idle_frame
        

        if goblin_main_rect.x > screen.get_width()-50:
            
            goblin_main_rect.x = -30


        if gold_pot_rect.x - goblin_main_rect.x < 100:
            return True


        planet1_frame, planet2_frame, planet3_frame, galaxy_frame = planet_frames(pl1, pl3)
        goblin_run_frame, goblin_attack_frame, goblin_death_frame, goblin_idle_frame, goblin_takehit_frame = goblin_frames(frame, frame2, frame3)
        goblin_THE_frame = pygame.transform.flip(goblin_THE_frame, moveLeft, False)



        if player_health <= 0:
            return False

        screen.fill(BLACK)

        ### SKY
        screen.blit(sky_img, (0, 0))
        
        # Planets
        screen.blit(planet1_frame, (screen_size[0] - 300, 100))
        screen.blit(planet2_frame, (screen_size[0]/2 - 180, screen_size[1] - 450)) 
        screen.blit(planet3_frame, (screen_size[0] - 1100, 120))  
        

        # GOBLIN
        screen.blit(goblin_THE_frame, goblin_main_rect)



        screen.blit(gold_pot, gold_pot_rect)

        ### GROUND
        screen.blit(ground_img, (ground_pos_x, 600))


        # Incrementing in variables for animation
        frame += 1        
        frame2 += 1
        pl1 += 1
        pl3 += 1


        # flip() updates the screen to make our changes visible
        pygame.display.update()
        
        # how many updates per second
        clock.tick(10)










if __name__ == "__main__":

    screen_size = (1200, 800)
    
    # create a window
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("pygame Test")

    # clock is used to set a max fps
    clock = pygame.time.Clock()


    game(screen, screen_size, clock, True)
    pygame.quit()
 
