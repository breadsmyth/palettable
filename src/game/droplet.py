import pygame

import constants
import draw.sprite


class Droplet:
    def __init__(self, color):
        self.color = color
        self.surf = draw.sprite.load('drop.png')

        # recolor the drop
        self.surf.fill(color, special_flags=pygame.BLEND_RGBA_MULT)

        specular = draw.sprite.load('specular.png')
        self.surf.blit(specular)

        # scale
        self.surf = pygame.transform.scale(
            self.surf,
            (constants.DROPLET_SIZE, constants.DROPLET_SIZE))

    def draw(self, screen, pos):
        screen.blit(self.surf, pos)
    
    def draw_at_mouse(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        pos = (
            mouse_pos[0] - constants.DROPLET_SIZE // 2,
            mouse_pos[1])
        
        self.draw(screen, pos)
