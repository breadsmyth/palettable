import pygame

import constants
import context.handler
import draw.text
import event
import gamestate


resolution = constants.RESOLUTION

display_flags = pygame.RESIZABLE

# initialize pygame
pygame.init()
gamestate.init()

screen = pygame.display.set_mode(resolution, display_flags)
pygame.display.set_caption(constants.WINDOW_TITLE)

# icon = pygame.image.load(os.path.join('assets', 'img', 'icon.png'))
# pygame.display.set_icon(icon)

clock = pygame.time.Clock()

# initialize everything else
draw.text.init()
context.handler.init()

# main window loop
while gamestate.running:
    screen.fill(constants.Color.BLACK)

    event.handle(pygame.event.get())

    context.handler.handle(screen)
    
    # event.draw_cursor(screen)

    pygame.display.flip()
    gamestate.time_elapsed += clock.tick(constants.FPS)
