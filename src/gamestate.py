import constants


def init():
    global clickables
    clickables = {}

    global current_context
    current_context = constants.Context.SPLASH

    global running
    running = True

    global time_elapsed
    time_elapsed = 0
