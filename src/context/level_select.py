import pygame

import constants
import draw.helpers


def init():
    global TITLE_TEXT
    TITLE_TEXT = draw.text.Text('Level Select', constants.TITLE_TEXT_SIZE)

def do(screen):
    draw.helpers.screen_border(screen)
    draw.helpers.title_text(screen, TITLE_TEXT)