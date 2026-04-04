import pygame

import constants
import context.handler
import draw.helpers
import draw.text
import game.button
import gamestate


def init():
    global TITLE_TEXT
    TITLE_TEXT = draw.text.Text(constants.TITLE, constants.TITLE_TEXT_SIZE)

    global START_BUTTON
    def start_onclick():
        context.handler.change_context(constants.Context.LEVELS)

    START_BUTTON = game.button.TextButton(
        draw.text.Text('Play', constants.BUTTON_TEXT_SIZE),
        start_onclick,
        constants.Context.TITLE)
    
    global CREDITS_BUTTON
    def credits_onclick():
        context.handler.change_context(constants.Context.CREDITS)

    CREDITS_BUTTON = game.button.TextButton(
        draw.text.Text('Credits', constants.BUTTON_TEXT_SIZE),
        credits_onclick,
        constants.Context.TITLE)

    global QUIT_BUTTON
    def quit_onclick():
        gamestate.running = False

    QUIT_BUTTON = game.button.TextButton(
        draw.text.Text('Quit', constants.BUTTON_TEXT_SIZE),
        quit_onclick,
        constants.Context.TITLE)


def do(screen):
    screen_size = screen.get_size()

    draw.helpers.screen_border(screen)

    draw.helpers.title_text(screen, TITLE_TEXT)

    button_width = min(
        screen_size[0] - (constants.BORDER_MARGIN*3 + constants.BORDER_WIDTH)*2,
        800)
    button_left = (screen_size[0] - button_width) // 2
    button_top = screen_size[1] // 2
    button_height = constants.BUTTON_TEXT_SIZE * 2

    START_BUTTON.draw(screen, pygame.Rect(
        button_left,
        button_top,
        button_width,
        button_height))

    CREDITS_BUTTON.draw(screen, pygame.Rect(
        button_left,
        button_top + button_height*2,
        button_width,
        button_height))

    QUIT_BUTTON.draw(screen, pygame.Rect(
        button_left,
        button_top + button_height*4,
        button_width,
        button_height))
