import pygame

import constants
import game.clickable


class PaletteSquare(game.clickable.Clickable):
    def __init__(self, rect, onclick, context):
        super().__init__(rect, onclick, context)

        size = (rect[2], rect[3])
        self.surf = pygame.Surface(size)
        self.surf.fill(constants.Color.WHITE)

    def draw(self, screen, rect):
        self.rect = rect

        screen.blit(self.surf, (rect[0], rect[1]))
    
    def recolor(self, color):
        self.surf.fill(color)