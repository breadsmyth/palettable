import constants
import draw.text


credits_font_size = 50

def init():
    global BACK_BUTTON
    BACK_BUTTON = draw.helpers.create_back_button(
        current_context=constants.Context.CREDITS,
        prev_context=constants.Context.TITLE)    

    global CREDIT_TEXT
    CREDIT_TEXT = [
        draw.text.Text('Made by Amy Starr in Pygame', credits_font_size),
        draw.text.Text('* * *', credits_font_size),
        draw.text.Text('Font: Poiret One', credits_font_size),
        draw.text.Text('Colors: Warm Neutrals from Coolors.co', credits_font_size),
    ]


def do(screen):
    screen.fill(constants.Color.WHITE)
    draw.helpers.draw_back_button(screen, BACK_BUTTON)

    for i, text in enumerate(CREDIT_TEXT):
        text.draw(screen, (
            constants.BORDER_MARGIN*2 + constants.BORDER_WIDTH,
            constants.BORDER_MARGIN*2 + constants.BORDER_WIDTH + i * credits_font_size*2
        ))
