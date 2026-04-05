import pygame

import constants
import context.handler
import game.droplet
import gamestate


def init():
    global DROP_1
    DROP_1 = game.droplet.Droplet((255, 0, 0))

    global DROP_2
    DROP_2 = game.droplet.Droplet((0, 255, 0))

    global DROP_3
    DROP_3 = game.droplet.Droplet((0, 0, 255))

    global DROP_4
    DROP_4 = game.droplet.Droplet((255, 255, 127))


def do(screen):
    screen_size = screen.get_size()

    screen.fill(constants.Color.PARCHMENT)
    screen.fill(constants.Color.WHITE, pygame.Rect(
        constants.BORDER_MARGIN,
        0,
        screen_size[0] - constants.BORDER_MARGIN*2,
        screen_size[1]))

    DROP_1.draw(screen, (100, 100))
    DROP_2.draw(screen, (200, 100))
    DROP_3.draw(screen, (300, 100))
    DROP_4.draw_at_mouse(screen)
