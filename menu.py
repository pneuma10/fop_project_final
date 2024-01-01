import pygame, sys
from toolmodule import *
from colors import *
from spritesheets import *
from fonts import *

# initialize pygame
pygame.init()


def main_menu2(screen, clock):
 
    
    play_btn_color = WHITE
    quit_btn_color = WHITE
    play = False
    p_height = 225 # to 350
 
    p_width = 60 # to 480
    text_pos_x = 600
    clock_speed = 10
    width = screen.get_width()
    small_planet_posx = - 300
    small_planet_posy = - 300
    ground_posy = 800
    goblin_posx = -200

    frame = 0
    frame2 = 0
    pl1 = 0
    pl3 = 0
    end_var = 0


    goblin_run_frame = get_image(goblin_run_spritesheet, frame, 150, 150, scale=2, colour = (0, 0, 0))
    goblin_idle_frame = get_image(goblin_idle_spritesheet, frame2, 150, 150, scale=2, colour = (0, 0, 0))
    goblin_THE_frame = goblin_run_frame


    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

        screen.fill(BLACK)

        if frame > 7:
            frame = 0
        if frame2 > 3:
            frame2 = 0 
        if pl1 > 149:
            pl1 = 0
        if pl3 > 80:
            pl3 = 0
        
        
        ### SKY
        screen.blit(sky_img, (0, 0))


        # MENU TEXTs
        menu_text = menu_font_large.render("MENU", 1, WHITE)
        play_text = menu_font_small.render("Play", 1, play_btn_color)
        quit_text = menu_font_small.render("Quit", 1, quit_btn_color)
        goblins_text = head_font_large.render("Goblin's", 1, WHITE)
        odyssey_text = head_font_large.render("Odyssey", 1, WHITE)


        screen.blit(goblins_text, (text_pos_x, 50))
        screen.blit(odyssey_text, (text_pos_x, 150))
        screen.blit(menu_text, (text_pos_x, 300))
   
               
        # CHECKING IF THE MENU BTNS ARE CLCIKED
            
        if event.type == pygame.MOUSEBUTTONDOWN: 
			
                #if the mouse is clicked on the 
                # button the game is terminated 

                # QUIT
                if width/2 <= mouse[0] <= width/2+(quit_text.get_width() + 20) and 500 <= mouse[1] <= 570: 
                    return False

                # PLAY
                if  width/2 <= mouse[0] <= width/2+(quit_text.get_width() + 20) and 420 <= mouse[1] <= 490: 
                    play = True

    
                    

        goblin_run_frame = get_image(goblin_run_spritesheet, frame, 150, 150, scale=2, colour = (0, 0, 0))
        goblin_idle_frame = get_image(goblin_idle_spritesheet, frame2, 150, 150, scale=2, colour = (0, 0, 0))




        if play:
            
            text_pos_x += 30

            if text_pos_x > 1200:


                if p_width < 440:
                    clock_speed = 20
                    p_height += 6
                    p_width += 20

                if small_planet_posx < 100:
                    small_planet_posx += 30
                    small_planet_posy += 30

                if ground_posy > 600:
                    ground_posy -= 10
                else:
                    if goblin_posx < -50:
                        goblin_THE_frame = goblin_run_frame
                        clock_speed = 10
                        goblin_posx += 3
                    else:
                        if end_var < 11:
                            end_var += 1
                            goblin_THE_frame = goblin_idle_frame
                        else:
                            return True
            

           
        
        # stores the (x,y) coordinates into 
        # the variable as a tuple 
        mouse = pygame.mouse.get_pos() 



        ### Menu btns changing color code
        # if mouse is hovered on a button it 
        # changes to lighter shade 
        # PLAY
        if width/2 <= mouse[0] <= width/2+(quit_text.get_width() + 20) and 420 <= mouse[1] <= 490: 
            play_btn_color = green_of_text

        else: 
            play_btn_color = WHITE

    
        # if mouse is hovered on a button it 
        # changes to lighter shade 
        # QUIT
        if width/2 <= mouse[0] <= width/2+(quit_text.get_width() + 20) and 500 <= mouse[1] <= 570: 
            quit_btn_color = green_of_text
            
        else: 
            quit_btn_color = WHITE


        ### Menu btn text
        screen.blit(play_text, (text_pos_x, 420))
        screen.blit(quit_text, (text_pos_x, 500))

        ### PLANETS ANIMATION (COMPLETED)
        planet1_frame = get_image(planet1_spritesheet, pl1, 100, 100, scale = 1, colour = (0, 0, 0))
        screen.blit(planet1_frame, (900, small_planet_posy))

        planet3_frame = get_image(planet3_spritesheet, pl3, 200, 200, scale = 1.4, colour = (0, 0, 0))
        screen.blit(planet3_frame, (small_planet_posx, 120))    

        planet2_frame = get_image(planet2_spritesheet, pl1, 100, 100, scale = 3.5, colour = (0, 0, 0))
        screen.blit(planet2_frame, (p_width, p_height))    


        ### GROUND
        screen.blit(ground_img, (0, ground_posy))

        #### GOBLIN MAIN CHARACTER
        screen.blit(goblin_THE_frame, (goblin_posx , 400))

  
        frame += 1        
        frame2 += 1
        pl1 += 1
        pl3 += 1

        # flip() updates the screen to make our changes visible
        pygame.display.update()
        
        # how many updates per second
        clock.tick(clock_speed)






if __name__ == "__main__":

    screen_size = (1200, 800)
    
    # create a window
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("pygame Test")

    # clock is used to set a max fps
    clock = pygame.time.Clock()


    main_menu2(screen, clock)
    pygame.quit()
 
