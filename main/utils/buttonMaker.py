import pygame
import pygame_gui


def make_button(text, x, y, manager,panel=None,BTN_W= 247 ,BTN_H = 81 ,id="",**anchors):
    return pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(x, y, BTN_W, BTN_H),
        text=text,
        manager=manager,
        container=panel,
        object_id=id,
        anchors={"centerx": "centerx", "top": "top", **anchors},
    )