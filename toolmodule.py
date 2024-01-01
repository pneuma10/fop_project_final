import pygame

pygame.init()

def get_image(sheet, frame, width, height, scale = 1, colour = None):

    ### for extraction of frame from sprite sheets
    image = pygame.Surface((width, height)).convert()
    image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(colour)

    return image