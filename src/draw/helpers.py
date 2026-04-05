import pygame

import constants
import context.handler
import draw.text
import game.button


def bordered_box(screen, rect, border_width, border_color, inner_color):
    screen.fill(border_color, rect)
    screen.fill(inner_color, pygame.Rect(
        rect[0] + border_width,
        rect[1] + border_width,
        rect[2] - border_width*2,
        rect[3] - border_width*2))

def create_back_button(current_context, prev_context):
    def back_onclick():
        context.handler.change_context(prev_context)
    
    return game.button.TextButton(
        draw.text.Text('Back', constants.BUTTON_TEXT_SIZE),
        back_onclick,
        current_context)

def draw_back_button(screen, button):
    screen_size = screen.get_size()

    button_width = min(
        screen_size[0] - (constants.BORDER_MARGIN*3 + constants.BORDER_WIDTH)*2,
        800)
    button_left = (screen_size[0] - button_width) // 2
    button_bottom = screen_size[1] - (constants.BORDER_MARGIN*2 + constants.BORDER_WIDTH)
    button_height = constants.BUTTON_TEXT_SIZE * 2

    button.draw(screen, pygame.Rect(
        button_left,
        button_bottom - button_height,
        button_width,
        button_height))

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
