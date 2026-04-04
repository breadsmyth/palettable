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
    MAIN = auto()
    SPLASH = auto()
    TITLE = auto()


FPS = 30
RESOLUTION = (800, 800)
TITLE = 'A Very Palettable Game'
WINDOW_TITLE = f'{TITLE} (demo)'
