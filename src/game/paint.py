import pygame

import constants
import draw.sprite
import game.colors


class Colorable:
    def __init__(self, color, filename):
        self.color = color.to_rgb()
        self.surf = draw.sprite.load(filename)

        # recolor
        self.surf.fill(self.color, special_flags=pygame.BLEND_RGBA_MULT)

        specular = draw.sprite.load('specular.png')
        self.surf.blit(specular)

        # scale
        self.surf = pygame.transform.scale(
            self.surf,
            (constants.COLORABLE_SIZE, constants.COLORABLE_SIZE))

    def draw(self, screen, pos):
        screen.blit(self.surf, pos)


class Bubble(Colorable):
    def __init__(self, color):
        super().__init__(color, 'circle.png')


class Droplet(Colorable):
    def __init__(self, color):
        super().__init__(color, 'drop.png')
    
    def draw_at_mouse(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        pos = (
            mouse_pos[0] - constants.DROPLET_SIZE // 2,
            mouse_pos[1])
        
        self.draw(screen, pos)
