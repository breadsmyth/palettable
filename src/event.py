import pygame

import gamestate


keys_pressed = {}

def draw_cursor(screen):
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(cursor_img, mouse_pos)


def handle(events):
    for event in events:
        if event.type == pygame.QUIT:
            gamestate.running = False
        
        elif event.type == pygame.KEYDOWN:
            keys_pressed[event.key] = True

            # Handle specific keypress
            if (event.key == pygame.K_ESCAPE and (
                    is_pressed(pygame.K_LCTRL) or
                    is_pressed(pygame.K_RCTRL))):
                # ctrl+esc = quit the program
                gamestate.running = False

        elif event.type == pygame.KEYUP:
            keys_pressed[event.key] = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left click
                # check to see whether the mouse is in a UI button
                for obj in gamestate.clickables[gamestate.current_context]:
                    if obj.is_moused():
                        obj.onclick()

            elif event.button == 3:  # right click
                pass
        
        elif event.type == pygame.MOUSEWHEEL:
            scroll_direction = event.y  # 1 or -1
            pass


def init():
    # global cursor_img
    # cursor_img = draw.sprite.load('cursor.png')
    pass


def is_pressed(key):
    global keys_pressed
    if key in keys_pressed.keys():
        return keys_pressed[key]
    
    return False
