import pygame

import constants
import context.handler
import draw.text
import game.button


TITLE_TEXT_SIZE = 50
BUTTON_TEXT_SIZE = 35

def init():
    global TITLE_TEXT
    TITLE_TEXT = draw.text.Text(constants.TITLE, TITLE_TEXT_SIZE)

    global START_BUTTON
    def start_onclick():
        context.handler.change_context(constants.Context.MAIN)

    START_BUTTON = game.button.TextButton(
        draw.text.Text('Play', BUTTON_TEXT_SIZE),
        start_onclick,
        constants.Context.TITLE)


def do(screen):
    screen_size = screen.get_size()
    border_margin = 50
    border_width = 20

    screen.fill(constants.Color.WHITE)
    screen.fill(constants.Color.SAND, pygame.Rect(
        border_margin,
        border_margin,
        screen_size[0] - border_margin*2,
        screen_size[1] - border_margin*2))
    screen.fill(constants.Color.WHITE, pygame.Rect(
        border_margin + border_width,
        border_margin + border_width,
        screen_size[0] - (border_margin + border_width)*2,
        screen_size[1] - (border_margin + border_width)*2))
    
    screen.fill(constants.Color.PARCHMENT, pygame.Rect(
        border_margin*2 + border_width,
        border_margin*2 + border_width,
        screen_size[0] - (border_margin*2 + border_width)*2,
        TITLE_TEXT_SIZE * 2))
    
    TITLE_TEXT.draw(screen, (
        border_margin*2 + border_width + border_margin//2,
        border_margin*2 + border_width + border_margin//2))

    button_left = border_margin*3 + border_width
    button_width = screen_size[0] - button_left*2
    button_top = screen_size[1] // 2
    button_height = 100

    START_BUTTON.draw(screen, pygame.Rect(
        button_left,
        button_top,
        button_width,
        button_height))
