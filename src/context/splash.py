import pygame

import constants
from context import handler
import draw.sprite
import gamestate


def init():
    global SPLASH_IMG
    SPLASH_IMG = draw.sprite.load('pygame_powered.png')

    global SPLASH_SIZE
    SPLASH_SIZE = SPLASH_IMG.get_size()

    global SPLASH_OVERLAY
    SPLASH_OVERLAY = pygame.Surface(
        size=SPLASH_SIZE,
        flags=pygame.SRCALPHA,
    )
    SPLASH_OVERLAY.fill((0, 0, 0, 0))

def do(screen):
    screen.fill((0, 0, 0))
    
    pos = (
        (screen.get_width() - SPLASH_SIZE[0]) // 2,
        (screen.get_height() - SPLASH_SIZE[1]) // 2)

    screen.blit(SPLASH_IMG, pos)
    
    # make the splash fade out
    if gamestate.time_elapsed >= 1000:
        alpha = min(255, int(
            (gamestate.time_elapsed - 1000)  # start fade-out at 1000ms
             / 1000  # fade-out lasts 1000ms
             * 255  # alpha goes from 0 to 255
        ))
        SPLASH_OVERLAY.fill((0, 0, 0, alpha))

    screen.blit(SPLASH_OVERLAY, pos)

    if gamestate.time_elapsed > 2000:
        handler.change_context(constants.Context.TITLE)
