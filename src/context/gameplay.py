import pygame

import constants
import draw.helpers
import draw.text
import game.colors
import game.paint
import gamestate


CANVAS_WIDTH = 600
PALETTE_WIDTH = 600 + 1
PALETTE_HEIGHT = 240 + 1

def init():
    global TITLE_TEXTS
    TITLE_TEXTS = []

    for i in range(1, constants.NUM_LEVELS+1):
        text = draw.text.Text(
            f'Level {i}',
            constants.TITLE_TEXT_SIZE)

        TITLE_TEXTS.append(text)

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
        screen_size[0] - 2*constants.BORDER_MARGIN,
        screen_size[1]))

    # calculations for drawing
    area_width = screen_size[0] - 2*constants.BORDER_MARGIN
    area_left = constants.BORDER_MARGIN

    canvas_top = (screen_size[1] * 2) // 10
    paint_top = (screen_size[1] * 7) // 10
    palette_top = (screen_size[1] * 8) // 10

    canvas_height = paint_top
    paint_height = palette_top - canvas_height
    palette_height = paint_height * 2
    
    # draw the surfaces
    surf_canvas = pygame.Surface((area_width, canvas_height))
    do_canvas(surf_canvas)
    screen.blit(surf_canvas, (area_left, canvas_top))

    draw.helpers.title_text(screen, TITLE_TEXTS[gamestate.current_level - 1])

    surf_paint = pygame.Surface((area_width, paint_height))
    do_paint(surf_paint)
    screen.blit(surf_paint, (area_left, paint_top))

    surf_palette = pygame.Surface((area_width, palette_height))
    do_palette(surf_palette)
    screen.blit(surf_palette, (area_left, palette_top))


def do_canvas(surf):
    area_size = surf.get_size()
    surf.fill(constants.Color.WHITE)

    canvas_size = (CANVAS_WIDTH, CANVAS_WIDTH)
    canvas_left = (area_size[0] - canvas_size[0]) // 2
    canvas_top = (area_size[1] - canvas_size[1]) // 2

    surf.fill(constants.Color.PARCHMENT, pygame.Rect(
        canvas_left,
        canvas_top,
        canvas_size[0],
        canvas_size[1]))


def do_paint(surf):
    area_size = surf.get_size()
    surf.fill(constants.Color.WHITE)

    paint_left = (area_size[0] - CANVAS_WIDTH) // 2
    paint_top = (area_size[1] - constants.COLORABLE_SIZE) // 2
    gap_width = (area_size[0] - 2*paint_left - 4*constants.COLORABLE_SIZE) // 3

    BUBBLE_CYAN.draw(surf, (paint_left, paint_top))
    BUBBLE_MAGENTA.draw(surf, (paint_left + (constants.COLORABLE_SIZE + gap_width), paint_top))
    BUBBLE_YELLOW.draw(surf, (paint_left + (constants.COLORABLE_SIZE + gap_width)*2, paint_top))
    BUBBLE_KEY.draw(surf, (paint_left + (constants.COLORABLE_SIZE + gap_width)*3, paint_top))


def do_palette(surf):
    area_size = surf.get_size()
    surf.fill(constants.Color.WHITE)

    palette_left = (area_size[0] - PALETTE_WIDTH) // 2 - 1
    palette_top = (area_size[1] - PALETTE_HEIGHT) // 2 - 1

    surf.fill(constants.Color.BLACK, pygame.Rect(
        palette_left,
        palette_top,
        PALETTE_WIDTH,
        PALETTE_HEIGHT))
