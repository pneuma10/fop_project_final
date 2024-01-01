import pygame

pygame.init()

pygame.display.set_mode((1200, 800))


### SKY
sky_img = pygame.image.load(r"Resources\Sky.png").convert()
sky_img = pygame.transform.scale(sky_img, (1400, 900))

### skull
skull_img = pygame.image.load(r"Resources\skull.webp").convert_alpha()
skull_img = pygame.transform.scale(skull_img, (300, 300))

### GROUND
ground_img = pygame.image.load(r"Resources\ground.png").convert()
ground_img = pygame.transform.scale(ground_img, (7000, 294))

### GOLDEN POT
gol_pot = pygame.image.load(r"Resources\golden pot.png").convert()

goldpot_spritesheet = pygame.image.load(r"Resources\Spritesheets\gold pot spritesheet.png").convert()


### CHARACTER SPRITE SHEET VARIABLES
# KNIGHT
# knight_spritesheet = pygame.image.load("")

# GOBLIN
# run, 1200X150, 8 frames
goblin_run_spritesheet = pygame.image.load(r"Resources\Spritesheets\Characters\Goblin\Run.png").convert()
# attack, 1200X150, 8 frames
goblin_attack_spritesheet = pygame.image.load(r"Resources\Spritesheets\Characters\Goblin\Attack.png").convert()
# death, 600X150, 4 frames
goblin_death_spritesheet = pygame.image.load(r"Resources\Spritesheets\Characters\Goblin\Death.png").convert() 
# idle, 600X150, 4 frames
goblin_idle_spritesheet = pygame.image.load(r"Resources\Spritesheets\Characters\Goblin\Idle.png").convert()
# Take Hit, 600X150, 4 frames
goblin_takehit_spritesheet = pygame.image.load(r"Resources\Spritesheets\Characters\Goblin\Take Hit.png").convert()

# SKELETON
# walk, 4 frames
skeleton_walk_spritesheet = pygame.image.load(r"Resources\Spritesheets\Characters\Skeleton\Walk.png").convert()
# attack, 1200X150, 8 frames
skeleton_attack_spritesheet = pygame.image.load(r"Resources\Spritesheets\Characters\Skeleton\Attack.png").convert()
# death, 600X150, 4 frames
skeleton_death_spritesheet = pygame.image.load(r"Resources\Spritesheets\Characters\Skeleton\Death.png").convert() 
# idle, 600X150, 4 frames
skeleton_idle_spritesheet = pygame.image.load(r"Resources\Spritesheets\Characters\Skeleton\Idle.png").convert()
# Take Hit, 600X150, 4 frames
skeleton_takehit_spritesheet = pygame.image.load(r"Resources\Spritesheets\Characters\Skeleton\Take Hit.png").convert()


# MUSHROOM
# run, 1200X150, 8 frames
mushroom_run_spritesheet = pygame.image.load(r"Resources\Spritesheets\Characters\Mushroom\Run.png").convert()
# attack, 1200X150, 8 frames
mushroom_attack_spritesheet = pygame.image.load(r"Resources\Spritesheets\Characters\Mushroom\Attack.png").convert()
# death, 600X150, 4 frames
mushroom_death_spritesheet = pygame.image.load(r"Resources\Spritesheets\Characters\Mushroom\Death.png").convert() 
# idle, 600X150, 4 frames
mushroom_idle_spritesheet = pygame.image.load(r"Resources\Spritesheets\Characters\Mushroom\Idle.png").convert()
# Take Hit, 600X150, 4 frames
mushroom_takehit_spritesheet = pygame.image.load(r"Resources\Spritesheets\Characters\Mushroom\Take Hit.png").convert()

# EYE
# flight, 8 frames
eye_flight_spritesheet = pygame.image.load(r"Resources\Spritesheets\Characters\Flying eye\Flight.png").convert()
# attack, 1200X150, 8 frames
eye_attack_spritesheet = pygame.image.load(r"Resources\Spritesheets\Characters\Flying eye\Attack.png").convert()
# death, 600X150, 4 frames
eye_death_spritesheet = pygame.image.load(r"Resources\Spritesheets\Characters\Flying eye\Death.png").convert() 
# Take Hit, 600X150, 4 frames
eye_takehit_spritesheet = pygame.image.load(r"Resources\Spritesheets\Characters\Flying eye\Take Hit.png").convert()

### PLANETS
# PLANET 1
planet1_spritesheet = pygame.image.load(r"Resources\Spritesheets\Planets\planet 1.png").convert()
planet2_spritesheet = pygame.image.load(r"Resources\Spritesheets\Planets\planet 2.png").convert()
planet3_spritesheet = pygame.image.load(r"Resources\Spritesheets\Planets\planet 3.png").convert()    
galaxy_spritesheet = pygame.image.load(r"Resources\Spritesheets\Planets\galaxy.png").convert()