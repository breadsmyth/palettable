from enum import Enum, auto


class Color:
    BLACK = (0, 0, 0)
    BRONZE = (203, 153, 126)
    GREEN = (183, 183, 164)
    LINEN = (255, 241, 230)
    PARCHMENT = (240, 239, 235)
    POWDER = (237, 220, 210)
    SAND = (221, 190, 169)
    WHITE = (255, 255, 255)


class Context(Enum):
    CREDITS = auto()
    GAMEPLAY = auto()
    LEVELS = auto()
    SPLASH = auto()
    TITLE = auto()


BORDER_MARGIN = 50
BORDER_WIDTH = 20
BUTTON_TEXT_SIZE = 35
COLORABLE_SIZE = 80
FPS = 30
RESOLUTION = (1000, 1600)
TITLE = 'A Very Palettable Game'
TITLE_TEXT_SIZE = 50
WINDOW_TITLE = f'{TITLE} (demo)'
