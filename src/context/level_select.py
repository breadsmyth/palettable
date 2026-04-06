import pygame

import constants
import context.handler
import draw.helpers
import draw.text
import game.button
import gamestate


row_length = 5

def select(level_num):
    gamestate.current_level = level_num
    context.handler.change_context(constants.Context.GAMEPLAY)


def init():
    global TITLE_TEXT
    TITLE_TEXT = draw.text.Text('Level Select', constants.TITLE_TEXT_SIZE)
    
    global BACK_BUTTON
    BACK_BUTTON = draw.helpers.create_back_button(
        current_context=constants.Context.LEVELS,
        prev_context=constants.Context.TITLE)

    global LEVEL_BUTTONS
    LEVEL_BUTTONS = []

    for i in range(1, constants.NUM_LEVELS+1):
        text = draw.text.Text(
            str(i),
            constants.BUTTON_TEXT_SIZE)

        def create_closure(level_num=i):
            def onclick():
                select(level_num)
            return onclick
        
        LEVEL_BUTTONS.append(game.button.TextButton(
            text,
            create_closure(),
            constants.Context.LEVELS))

def do(screen):
    draw.helpers.screen_border(screen)
    draw.helpers.title_text(screen, TITLE_TEXT)
    draw.helpers.draw_back_button(screen, BACK_BUTTON)

    area_left = constants.BORDER_MARGIN + constants.BORDER_WIDTH
    gap_width = (screen.get_width()
        - 2*area_left
        - row_length * constants.BUTTON_TEXT_SIZE*2) // (row_length + 1)

    for i, button in enumerate(LEVEL_BUTTONS):
        button.draw(screen, pygame.Rect(
            area_left + gap_width + (i%row_length) * (
                gap_width + constants.BUTTON_TEXT_SIZE*2),
            300 + 4*constants.BUTTON_TEXT_SIZE * (i//row_length),
            constants.BUTTON_TEXT_SIZE*2,
            constants.BUTTON_TEXT_SIZE*2))
    
