import constants
from context import credits_screen, gameplay, level_select, splash, title
import gamestate


def change_context(new_context):
    gamestate.current_context = new_context


def handle(screen):
    match gamestate.current_context:
        case constants.Context.CREDITS:
            credits_screen.do(screen)
        case constants.Context.GAMEPLAY:
            gameplay.do(screen)
        case constants.Context.LEVELS:
            level_select.do(screen)
        case constants.Context.SPLASH:
            splash.do(screen)
        case constants.Context.TITLE:
            title.do(screen)


def init():
    for context in constants.Context:
        gamestate.clickables[context] = []

    credits_screen.init()
    gameplay.init()
    level_select.init()
    splash.init()
    title.init()
