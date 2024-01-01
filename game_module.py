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

    s1death, s2death, s3death, s4death, m1death, m2death, m3death = 0, 0, 0, 0, 0, 0, 0

    player_health = 400


    moveRight, moveLeft, moveRight, moveDown, fight = False, False, False, False, False

  

    ### MAIN CHARACTER GOBLIN
    goblin_idle_frame = goblin_frames(0, 0, 0)[3]
    goblin_THE_frame = goblin_idle_frame
    goblin_main_rect = goblin_THE_frame.get_rect(midbottom = (100, 697))

    ### SKELETON 1
    skeleton1_main_frame = skeleton_frames(0, 0, 0)[3]
    skeleton1_main_rect = skeleton1_main_frame.get_rect(midbottom = (1600, 697))
    skeleton1_health = 20
    ### SKELETON 2
    skeleton2_main_frame = skeleton_frames(0, 0, 0)[3]
    skeleton2_main_rect = skeleton2_main_frame.get_rect(midbottom = (2000, 697))
    skeleton2_health = 20
    ### SKELETON 3
    skeleton3_main_frame = skeleton_frames(0, 0, 0)[3]
    skeleton3_main_rect = skeleton3_main_frame.get_rect(midbottom = (2700, 697))
    skeleton3_health = 20
    ### SKELETON 4
    skeleton4_main_frame = skeleton_frames(0, 0, 0)[3]
    skeleton4_main_rect = skeleton4_main_frame.get_rect(midbottom = (3000, 697))
    skeleton4_health = 20


    ### MUSHROOM 1
    mushroom1_main_frame = mushroom_frames(0, 0, 0)[3]
    mushroom1_main_rect = mushroom1_main_frame.get_rect(midbottom = (2000, 670))
    mush1_health = 30
    ### MUSHROOM 2
    mushroom2_main_frame = mushroom_frames(0, 0, 0)[3]
    mushroom2_main_rect = mushroom2_main_frame.get_rect(midbottom = (2500, 670))
    mush2_health = 30
    ### MUSHROOM 3
    mushroom3_main_frame = mushroom_frames(0, 0, 0)[3]
    mushroom3_main_rect = mushroom3_main_frame.get_rect(midbottom = (3000, 670))
    mush3_health = 30


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
                if event.key == K_UP:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN:
                    moveUp = False
                    moveDown = True
                if event.key == K_Z:
                    fight = True
            if event.type == pygame.KEYUP:
                if event.key == K_LEFT:
                    moveLeft = False
                if event.key == K_RIGHT:
                    moveRight = False
                if event.key == K_UP:
                    moveUp = False
                if event.key == K_DOWN:
                    moveDown = False
                if event.key == K_Z:
                    fight = False
            else:
                pass


        if fight:
            

            if moveRight:
                if goblin_main_rect.x < 200 or gold_pot_rect.x <= 1050:
                    goblin_main_rect.x += 3

                if gold_pot_rect.x > 1050:
                    gold_pot_rect.x -= 3

                    skeleton1_main_rect.x -= 3
                    skeleton2_main_rect.x -= 3
                    skeleton3_main_rect.x -= 3
                    skeleton4_main_rect.x -= 3

                    mushroom1_main_rect.x -= 3
                    mushroom2_main_rect.x -= 3
                    mushroom3_main_rect.x -= 3
                

                    if not goblin_main_rect.x < 200:
                        ground_pos_x -= 3

            if moveLeft:
                goblin_main_rect.x -= 3

            goblin_THE_frame = goblin_attack_frame  


            ### MAIN CHARACTER ATTACKING ENEMIES CODE
            if 70 > goblin_main_rect.x - skeleton1_main_rect.x and goblin_main_rect.x - skeleton1_main_rect.x > -70:
                skeleton1_health -= 1
            if 70 > goblin_main_rect.x - skeleton2_main_rect.x and goblin_main_rect.x - skeleton2_main_rect.x > -70:
                skeleton2_health -= 1
            if 70 > goblin_main_rect.x - skeleton3_main_rect.x and goblin_main_rect.x - skeleton3_main_rect.x > -70:
                skeleton3_health -= 1
            if 70 > goblin_main_rect.x - skeleton4_main_rect.x and goblin_main_rect.x - skeleton4_main_rect.x > -70:
                skeleton4_health -= 1

            if 70 > goblin_main_rect.x - mushroom1_main_rect.x and goblin_main_rect.x - mushroom1_main_rect.x > -70:
                mush1_health -= 1
            if 70 > goblin_main_rect.x - mushroom2_main_rect.x and goblin_main_rect.x - mushroom2_main_rect.x > -70:
                mush2_health -= 1
            if 70 > goblin_main_rect.x - mushroom3_main_rect.x and goblin_main_rect.x - mushroom3_main_rect.x > -70:
                mush3_health -= 1

            #print(f"sk1: {skeleton1_health}, sk2: {skeleton2_health}, sk3: {skeleton3_health}, sk4: {skeleton4_health}, m1: {mush1_health}, m2: {mush2_health}, m3: {mush3_health}")
            

        elif moveRight:

            if goblin_main_rect.x < 200 or gold_pot_rect.x <= 1050:
                goblin_main_rect.x += 10



            if gold_pot_rect.x > 1050:
                gold_pot_rect.x -= 10

                skeleton1_main_rect.x -= 10
                skeleton2_main_rect.x -= 10
                skeleton3_main_rect.x -= 10
                skeleton4_main_rect.x -= 10

                mushroom1_main_rect.x -= 10
                mushroom2_main_rect.x -= 10
                mushroom3_main_rect.x -= 10
              

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


        if gold_pot_rect.x - goblin_main_rect.x < 100 and skeleton1_health <= 0 and skeleton2_health <= 0 and skeleton3_health <= 0 and skeleton4_health <= 0 and mush1_health <= 0 and mush2_health <= 0 and mush3_health <= 0:
            
            return True



        ### FRAMES
        skeleton_attack_frame, skeleton_walk_frame, skeleton_death_frame, skeleton_idle_frame, skeleton_takehit_frame = skeleton_frames(frame, frame2, frame3)
        mushroom_run_frame, mushroom_attack_frame, mushroom_death_frame, mushroom_idle_frame, mushroom_takehit_frame = mushroom_frames(frame, frame2, frame3)
        eye_flight_frame, eye_attack_frame, eye_death_frame, eye_takehit_frame = eye_frames(frame, frame2)
        planet1_frame, planet2_frame, planet3_frame, galaxy_frame = planet_frames(pl1, pl3)
        goblin_run_frame, goblin_attack_frame, goblin_death_frame, goblin_idle_frame, goblin_takehit_frame = goblin_frames(frame, frame2, frame3)
        goblin_THE_frame = pygame.transform.flip(goblin_THE_frame, moveLeft, False)



        ### ENEMY MOVEMENTS
        ## SKELETON 1
        if skeleton1_health > 0:

            if skeleton1_main_rect.x - goblin_main_rect.x < 600 and skeleton1_main_rect.x > goblin_main_rect.x +50:
                skeleton1_main_frame = skeleton_walk_frame
                skeleton1_main_rect.x -= 5

            if skeleton1_main_rect.x - goblin_main_rect.x < 70:
                skeleton1_main_frame = skeleton_attack_frame
                player_health -= 0.7

            if skeleton1_main_rect.x < goblin_main_rect.x:
            

                if skeleton1_main_rect.x - goblin_main_rect.x < -50:
                    skeleton1_main_frame = skeleton_walk_frame
                    skeleton1_main_rect.x += 5

                skeleton1_main_frame = pygame.transform.flip(skeleton1_main_frame, True, False)
        else:

            skeleton1_main_frame = skeleton_frames(frame, frame, s1death)[2]
            if s1death < 3:
                s1death += 1


        ## SKELETON 2
        if skeleton2_health > 0:
            if skeleton2_main_rect.x - goblin_main_rect.x < 600 and skeleton2_main_rect.x > goblin_main_rect.x +60:
                skeleton2_main_frame = skeleton_walk_frame
                skeleton2_main_rect.x -= 5

            if skeleton2_main_rect.x - goblin_main_rect.x < 70:
                skeleton2_main_frame = skeleton_attack_frame
                player_health -= 0.7

            if skeleton2_main_rect.x < goblin_main_rect.x:
                

                if skeleton2_main_rect.x - goblin_main_rect.x < -70:
                    skeleton2_main_frame = skeleton_walk_frame
                    skeleton2_main_rect.x += 5

                skeleton2_main_frame = pygame.transform.flip(skeleton2_main_frame, True, False)

        else:

            skeleton2_main_frame = skeleton_frames(frame, frame, s2death)[2]
            if s2death < 3:
                s2death += 1


        ## SKELETON 3
        if skeleton3_health > 0:
            if skeleton3_main_rect.x - goblin_main_rect.x < 600 and skeleton3_main_rect.x > goblin_main_rect.x +60:
                skeleton3_main_frame = skeleton_walk_frame
                skeleton3_main_rect.x -= 5

            if skeleton3_main_rect.x - goblin_main_rect.x < 70:
                skeleton3_main_frame = skeleton_attack_frame
                player_health -= 0.7

            if skeleton3_main_rect.x < goblin_main_rect.x:
                

                if skeleton3_main_rect.x - goblin_main_rect.x < -70:
                    skeleton3_main_frame = skeleton_walk_frame
                    skeleton3_main_rect.x += 5

                skeleton3_main_frame = pygame.transform.flip(skeleton3_main_frame, True, False)

        else:

            skeleton3_main_frame = skeleton_frames(frame, frame, s3death)[2]
            if s3death < 3:
                s3death += 1

        
        
        ## SKELETON 4
        if skeleton4_health > 0:
            if skeleton4_main_rect.x - goblin_main_rect.x < 600 and skeleton4_main_rect.x > goblin_main_rect.x +60:
                skeleton4_main_frame = skeleton_walk_frame
                skeleton4_main_rect.x -= 5

            if skeleton4_main_rect.x - goblin_main_rect.x < 70:
                skeleton4_main_frame = skeleton_attack_frame
                player_health -= 0.7

            if skeleton4_main_rect.x < goblin_main_rect.x:
                

                if skeleton4_main_rect.x - goblin_main_rect.x < -70:
                    skeleton4_main_frame = skeleton_walk_frame
                    skeleton4_main_rect.x += 5

                skeleton4_main_frame = pygame.transform.flip(skeleton4_main_frame, True, False)
        else:

            skeleton4_main_frame = skeleton_frames(frame, frame, s4death)[2]
            if s4death < 3:
                s4death += 1






        ## MUSHROOM 1
        if mush1_health > 0:
            if mushroom1_main_rect.x - goblin_main_rect.x < 500 and mushroom1_main_rect.x > goblin_main_rect.x +40:
                mushroom1_main_frame = mushroom_run_frame
                mushroom1_main_rect.x -= 7

            if mushroom1_main_rect.x - goblin_main_rect.x < 70:
                mushroom1_main_frame = mushroom_attack_frame
                player_health -= 0.5

            if mushroom1_main_rect.x < goblin_main_rect.x:
                
                if mushroom1_main_rect.x - goblin_main_rect.x < -35:
                    mushroom1_main_frame = mushroom_run_frame
                    mushroom1_main_rect.x += 7

                mushroom1_main_frame = pygame.transform.flip(mushroom1_main_frame, True, False)

        else:

            mushroom1_main_frame = mushroom_frames(frame, frame, m1death)[2]
            if m1death < 3:
                m1death += 1



        ## MUSHROOM 2
        if mush2_health > 0:

            if mushroom2_main_rect.x - goblin_main_rect.x < 500 and mushroom2_main_rect.x > goblin_main_rect.x +50:
                mushroom2_main_frame = mushroom_run_frame
                mushroom2_main_rect.x -= 7

            if mushroom2_main_rect.x - goblin_main_rect.x < 70:
                mushroom2_main_frame = mushroom_attack_frame
                player_health -= 0.5

            if mushroom2_main_rect.x < goblin_main_rect.x:
                
                if mushroom2_main_rect.x - goblin_main_rect.x < -20:
                    mushroom2_main_frame = mushroom_run_frame
                    mushroom2_main_rect.x += 7

                mushroom2_main_frame = pygame.transform.flip(mushroom2_main_frame, True, False)
        
        else:

            mushroom2_main_frame = mushroom_frames(frame, frame, m2death)[2]
            if m2death < 3:
                m2death += 1


        ## MUSHROOM 3
        if mush3_health > 0:
            if mushroom3_main_rect.x - goblin_main_rect.x < 500 and mushroom3_main_rect.x > goblin_main_rect.x +30:
                mushroom3_main_frame = mushroom_run_frame
                mushroom3_main_rect.x -= 7

            if mushroom3_main_rect.x - goblin_main_rect.x < 70:
                mushroom3_main_frame = mushroom_attack_frame
                player_health -= 0.5

            if mushroom3_main_rect.x < goblin_main_rect.x:
                
                if mushroom3_main_rect.x - goblin_main_rect.x < -10:
                    mushroom3_main_frame = mushroom_run_frame
                    mushroom3_main_rect.x += 7

                mushroom3_main_frame = pygame.transform.flip(mushroom3_main_frame, True, False)
        
        else:

            mushroom3_main_frame = mushroom_frames(frame, frame, m3death)[2]
            if m3death < 3:
                m3death += 1



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

        # Enemies

        screen.blit(skeleton1_main_frame, skeleton1_main_rect)        
        screen.blit(skeleton2_main_frame, skeleton2_main_rect)     
        screen.blit(skeleton3_main_frame, skeleton3_main_rect)
        screen.blit(skeleton4_main_frame, skeleton4_main_rect)

        screen.blit(mushroom1_main_frame, mushroom1_main_rect)
        screen.blit(mushroom2_main_frame, mushroom2_main_rect)
        screen.blit(mushroom3_main_frame, mushroom3_main_rect)

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
 
