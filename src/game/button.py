import pygame

import constants
import game.clickable


class Button(game.clickable.Clickable):
    def __init__(self, onclick, context):
        super().__init__(pygame.Rect(0, 0, 0, 0), onclick, context)

    def draw(self, surf, rect):
        self.rect = rect

        color = constants.Color.POWDER
        if self.is_moused():
            color = constants.Color.SAND

        surf.fill(color, self.rect)


class TextButton(Button):
    def __init__(self, text, onclick, context):
        self.text = text
        super().__init__(onclick, context)
    
    def draw(self, surf, rect):
        super().draw(surf, rect)
        
        rect_pos = (self.rect[0], self.rect[1])
        rect_size = (self.rect[2], self.rect[3])

        text_size = self.text.surf.get_size()

        text_pos = (
            rect_pos[0] + (rect_size[0] - text_size[0]) // 2,
            rect_pos[1] + (rect_size[1] - text_size[1]) // 2)

        self.text.draw(surf, text_pos)
