
from utils.buttonMaker import make_button

import pygame
import pygame_gui

class HomePanel:
    def __init__(self,manager,win):
        self.manager = manager
        self.win = win

        wi,h= self.win.screen.get_size()
        self.panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(0,-50, wi, 820),
            manager=self.manager,
            object_id="#homePanel",
            anchors={  "centerx": "centerx", "centery": "centery"}

        )
        w = self.panel.get_abs_rect().width
        self.panelTitle = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(0, 0, w, 160),
            manager=self.manager,
            container=self.panel,
            object_id="#panelTitle",
            anchors={"centerx": "centerx", "top": "top"}
        )

        self.titleLabel = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, 0, 700, 160),
            text="Snake Game",
            manager=self.manager,
            container=self.panelTitle,
            object_id="#title",
            anchors={"center": "center"},
        )

        self.panelButton = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(0, 190, w, 300),
            manager=self.manager,
            container=self.panel,
            object_id="#panelButton",
            anchors={"centerx": "centerx", "top": "top"}
        )

        self.play_button = make_button("Play", 0, 0, self.manager, panel=self.panelButton)
        self.infos_button = make_button("Infos", 0, 86, self.manager,panel=self.panelButton)
        self.settings_button = make_button("Settings", 0, 172, self.manager, panel=self.panelButton)

    def show(self):
        self.panel.show()

    def kill(self):
        self.panel.kill()

    def handleEvent(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:

            match event.ui_element:
                case self.play_button:
                    print("Play")
                    self.win.navigationPanel("level")
                case self.infos_button:
                    self.win.navigationPanel("infos")

                case self.settings_button:
                    self.win.navigationPanel("settings")


