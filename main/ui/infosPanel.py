import pygame
import pygame_gui
from utils.buttonMaker import make_button

class InfosPanel:
    def __init__(self,manager, win):
        self.manager=manager
        self.win=win
        self.panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(0, -50, 700, 800),
            manager=self.manager,
            object_id="#infosPanel",
            anchors={"center": "center"}
        )
        self.text = pygame_gui.elements.UITextBox("Game made by ...",
                                                  manager=self.manager,
                                                  container=self.panel,
                                                  relative_rect=pygame.Rect(0, 40, 650, 420),
                                                  anchors={"center_x": "center_x", "center_y": "center_y"}
                                                  )
        self.panelButton = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(0, 90,700 , 130),
            manager=self.manager,
            container=self.panel,
            object_id="#panelButton",
            anchors={"centerx": "centerx", "top_target": self.text},
        )

        self.back_button = make_button("←", 0, 0, self.manager, panel=self.panelButton, object_id="#backButton")

    def show(self):
        self.panel.show()

    def kill(self):
        self.panel.kill()

    def handleEvent(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            match event.ui_element:
                case self.back_button:
                    self.win.navigationPanel("home")
