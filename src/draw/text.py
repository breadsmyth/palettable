import os
import pygame
from pygame import freetype

import constants


FONT_PATH = os.path.join('assets', 'PoiretOne-Regular.ttf')

def init():
    global font
    freetype.init()
    
    font = freetype.Font(FONT_PATH)


class Text:
    def __init__(self,
                 text,
                 size,
                 color=constants.Color.BLACK):
        self.surf, rect = font.render(
            text,
            color,
            size=size)
        
        self.width, self.height = self.surf.get_size()
        self.text = text
    
    def draw(self, surf, pos):
        surf.blit(self.surf, pos)
