import pygame

import constants
import context.handler
import draw.text
import game.button


credits_font_size = 50

def init():
    global BACK_BUTTON
    def back_onclick():
        context.handler.change_context(constants.Context.TITLE)
    
    BACK_BUTTON = game.button.TextButton(
        draw.text.Text('Back', constants.BUTTON_TEXT_SIZE),
        back_onclick,
        constants.Context.CREDITS)

    global CREDIT_TEXT
    CREDIT_TEXT = [
        draw.text.Text('Made in Pygame by Amy Starr', credits_font_size),
        draw.text.Text('* * *', credits_font_size),
        draw.text.Text('Font: Poiret One', credits_font_size),
        draw.text.Text('Colors: Warm Neutrals from Coolors.co', credits_font_size),
    ]


def do(screen):
    screen.fill(constants.Color.WHITE)

    screen_size = screen.get_size()

    # draw back button
    button_width = min(
        screen_size[0] - (constants.BORDER_MARGIN*3 + constants.BORDER_WIDTH)*2,
        800)
    button_left = (screen_size[0] - button_width) // 2
    button_bottom = screen_size[1] - (constants.BORDER_MARGIN*2 + constants.BORDER_WIDTH)
    button_height = constants.BUTTON_TEXT_SIZE * 2

    BACK_BUTTON.draw(screen, pygame.Rect(
        button_left,
        button_bottom - button_height,
        button_width,
        button_height))

    # draw credits
    for i, text in enumerate(CREDIT_TEXT):
        text.draw(screen, (
            constants.BORDER_MARGIN*2 + constants.BORDER_WIDTH,
            constants.BORDER_MARGIN*2 + constants.BORDER_WIDTH + i * credits_font_size*2
        ))
