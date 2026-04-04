import pygame

import gamestate


class Clickable:
    def __init__(self, rect, onclick, context):
        self.rect = rect
        self.onclick = onclick
        gamestate.clickables[context].append(self)
    
    def is_moused(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)
