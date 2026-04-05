import pygame

import constants
import context.handler
import game.colors
import game.paint
import gamestate


def init():
    global BUBBLE_CYAN
    BUBBLE_CYAN = game.paint.Bubble(game.colors.CMYK(100, 0, 0, 0))

    global BUBBLE_MAGENTA
    BUBBLE_MAGENTA = game.paint.Bubble(game.colors.CMYK(0, 100, 0, 0))

    global BUBBLE_YELLOW
    BUBBLE_YELLOW = game.paint.Bubble(game.colors.CMYK(0, 0, 100, 0))

    global BUBBLE_KEY
    BUBBLE_KEY = game.paint.Bubble(game.colors.CMYK(0, 0, 0, 100))


def do(screen):
    screen_size = screen.get_size()

    screen.fill(constants.Color.PARCHMENT)
    screen.fill(constants.Color.WHITE, pygame.Rect(
        constants.BORDER_MARGIN,
        0,
        screen_size[0] - constants.BORDER_MARGIN*2,
        screen_size[1]))

    # calculations for drawing
    area_width = screen_size[0] - 2*constants.BORDER_MARGIN
    area_left = constants.BORDER_MARGIN

    canvas_top = 0
    paint_top = (screen_size[1] * 7) // 10
    palette_top = (screen_size[1] * 8) // 10

    canvas_height = paint_top
    paint_height = palette_top
    palette_height = paint_height * 2
    
    # draw the surfaces
    surf_canvas = pygame.Surface((area_width, canvas_height))
    do_canvas(surf_canvas)
    screen.blit(surf_canvas, (area_left, canvas_top))

    surf_paint = pygame.Surface((area_width, paint_height))
    do_paint(surf_paint)
    screen.blit(surf_paint, (area_left, paint_top))

    surf_palette = pygame.Surface((area_width, palette_height))
    do_palette(surf_palette)
    screen.blit(surf_palette, (area_left, palette_top))


def do_canvas(surf):
    area_size = surf.get_size()
    surf.fill(constants.Color.LINEN)


def do_paint(surf):
    area_size = surf.get_size()
    surf.fill(constants.Color.POWDER)


def do_palette(surf):
    area_size = surf.get_size()
    surf.fill(constants.Color.SAND)
