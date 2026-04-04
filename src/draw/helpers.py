import pygame

import constants


def bordered_box(screen, rect, border_width, border_color, inner_color):
    screen.fill(border_color, rect)
    screen.fill(inner_color, pygame.Rect(
        rect[0] + border_width,
        rect[1] + border_width,
        rect[2] - border_width*2,
        rect[3] - border_width*2))

def screen_border(screen):
    screen_size = screen.get_size()

    screen.fill(constants.Color.WHITE)

    bordered_box(
        screen,
        pygame.Rect(
            constants.BORDER_MARGIN,
            constants.BORDER_MARGIN,
            screen_size[0] - constants.BORDER_MARGIN*2,
            screen_size[1] - constants.BORDER_MARGIN*2),
        constants.BORDER_WIDTH,
        constants.Color.SAND,
        constants.Color.WHITE)

def title_text(screen, text):
    screen_size = screen.get_size()

    screen.fill(constants.Color.PARCHMENT, pygame.Rect(
        constants.BORDER_MARGIN*2 + constants.BORDER_WIDTH,
        constants.BORDER_MARGIN*2 + constants.BORDER_WIDTH,
        screen_size[0] - (constants.BORDER_MARGIN*2 + constants.BORDER_WIDTH)*2,
        constants.TITLE_TEXT_SIZE * 2))
    
    text.draw(screen, (
        constants.BORDER_MARGIN*2 + constants.BORDER_WIDTH + constants.BORDER_MARGIN//2,
        constants.BORDER_MARGIN*2 + constants.BORDER_WIDTH + constants.BORDER_MARGIN//2))
