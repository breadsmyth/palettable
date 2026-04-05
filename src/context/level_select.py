import pygame

import constants
import draw.helpers
import draw.text
import game.button


num_levels = 20
row_length = 5

def init():
    global TITLE_TEXT
    TITLE_TEXT = draw.text.Text('Level Select', constants.TITLE_TEXT_SIZE)

    global LEVEL_BUTTONS
    LEVEL_BUTTONS = []

    def select(level_num):
        print(f'Selected level {level_num}!')

    for i in range(1, num_levels+1):
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