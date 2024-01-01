import pygame
from spritesheets import *
from toolmodule import *
from colors import *


def golden_pot():
    gold_pot = get_image(gol_pot, 0, 800, 800, scale=0.1, colour=BLACK)
    return gold_pot

def planet_frames(pl1, pl3):
        ### PLANETS ANIMATION (COMPLETED)
        planet1_frame = get_image(planet1_spritesheet, pl1, 100, 100, scale = 1, colour = (0, 0, 0))
    
        planet2_frame = get_image(planet2_spritesheet, pl1, 100, 100, scale = 3.5, colour = (0, 0, 0))
           
        planet3_frame = get_image(planet3_spritesheet, pl3, 200, 200, scale = 1.4, colour = (0, 0, 0))
        
        galaxy_frame = get_image(galaxy_spritesheet, pl1, 100, 100, scale = 2, colour = (0, 0, 0))

        return planet1_frame, planet2_frame, planet3_frame, galaxy_frame


def goblin_frames(frame, frame2, frame3):
            # ### GOBLIN MAIN CHARACTER FRAMES
        goblin_run_frame = get_image(goblin_run_spritesheet, frame, 150, 150, scale=2, colour = (0, 0, 0))
        goblin_attack_frame = get_image(goblin_attack_spritesheet, frame, 150, 150, scale=2, colour = (0, 0, 0))
        goblin_death_frame = get_image(goblin_death_spritesheet, frame3, 150, 150, scale=2, colour = (0, 0, 0))
        goblin_idle_frame = get_image(goblin_idle_spritesheet, frame2, 150, 150, scale=2, colour = (0, 0, 0))
        goblin_takehit_frame = get_image(goblin_takehit_spritesheet, frame2, 150, 150, scale=2, colour = (0, 0, 0))

        return goblin_run_frame, goblin_attack_frame, goblin_death_frame, goblin_idle_frame, goblin_takehit_frame




def skeleton_frames(frame, frame2, frame3):
    ### SKELETON
    skeleton_attack_frame = get_image(skeleton_attack_spritesheet, frame, 150, 150, scale=2, colour = (0, 0, 0))
    skeleton_attack_frame = pygame.transform.flip(skeleton_attack_frame, True, False)
    skeleton_walk_frame = get_image(skeleton_walk_spritesheet, frame2, 150, 150, scale=2, colour = (0, 0, 0))
    skeleton_walk_frame = pygame.transform.flip(skeleton_walk_frame, True, False)
    skeleton_death_frame = get_image(skeleton_death_spritesheet, frame3, 150, 150, scale=2, colour = (0, 0, 0))
    skeleton_death_frame = pygame.transform.flip(skeleton_death_frame, True, False)
    skeleton_idle_frame = get_image(skeleton_idle_spritesheet, frame2, 150, 150, scale=2, colour = (0, 0, 0))
    skeleton_idle_frame = pygame.transform.flip(skeleton_idle_frame, True, False)
    skeleton_takehit_frame = get_image(skeleton_takehit_spritesheet, frame2, 150, 150, scale=2, colour = (0, 0, 0))
    skeleton_takehit_frame = pygame.transform.flip(skeleton_takehit_frame, True, False)

    return skeleton_attack_frame, skeleton_walk_frame, skeleton_death_frame, skeleton_idle_frame, skeleton_takehit_frame


def mushroom_frames(frame, frame2, frame3):
    ### mushroom

    mushroom_run_frame = get_image(mushroom_run_spritesheet, frame, 150, 150, scale=1.5, colour = (0, 0, 0))
    mushroom_run_frame = pygame.transform.flip(mushroom_run_frame, True, False)
    mushroom_attack_frame = get_image(mushroom_attack_spritesheet, frame, 150, 150, scale=1.5, colour = (0, 0, 0))
    mushroom_attack_frame = pygame.transform.flip(mushroom_attack_frame, True, False)
    mushroom_death_frame = get_image(mushroom_death_spritesheet, frame3, 150, 150, scale=1.5, colour = (0, 0, 0))
    mushroom_death_frame = pygame.transform.flip(mushroom_death_frame, True, False)
    mushroom_idle_frame = get_image(mushroom_idle_spritesheet, frame2, 150, 150, scale=1.5, colour = (0, 0, 0))
    mushroom_idle_frame = pygame.transform.flip(mushroom_idle_frame, True, False)
    mushroom_takehit_frame = get_image(mushroom_takehit_spritesheet, frame2, 150, 150, scale=1.5, colour = (0, 0, 0))
    mushroom_takehit_frame = pygame.transform.flip(mushroom_takehit_frame, True, False)

    return mushroom_run_frame, mushroom_attack_frame, mushroom_death_frame, mushroom_idle_frame, mushroom_takehit_frame

def eye_frames(frame, frame2):
    ### EYE

    eye_flight_frame = get_image(eye_flight_spritesheet, frame, 150, 150, scale=1.5, colour = (0, 0, 0))
    eye_flight_frame = pygame.transform.flip(eye_flight_frame, True, False)
    eye_attack_frame = get_image(eye_attack_spritesheet, frame, 150, 150, scale=1.5, colour = (0, 0, 0))
    eye_attack_frame = pygame.transform.flip(eye_attack_frame, True, False)
    eye_death_frame = get_image(eye_death_spritesheet, frame2, 150, 150, scale=1.5, colour = (0, 0, 0))
    eye_death_frame = pygame.transform.flip(eye_death_frame, True, False)
    eye_takehit_frame = get_image(eye_takehit_spritesheet, frame2, 150, 150, scale=1.5, colour = (0, 0, 0))
    eye_takehit_frame = pygame.transform.flip(eye_takehit_frame, True, False)

    return eye_flight_frame, eye_attack_frame, eye_death_frame, eye_takehit_frame