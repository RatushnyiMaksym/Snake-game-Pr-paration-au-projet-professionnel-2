import pygame
import pygame_gui
from utils.buttonMaker import make_button

class SettingsPanel:
    def __init__(self,manager,win):
        self.manager=manager
        self.win=win

        wi, h = self.win.screen.get_size()
        self.panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(0, -50, wi, 820),
            manager=self.manager,
            object_id="#settingPanel",
            anchors={"centerx": "centerx", "centery": "centery"}

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
            text="Settings",
            manager=self.manager,
            container=self.panelTitle,
            object_id="#title",
            anchors={"center": "center"},
        )
        self.panelButton = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(0, 590, self.panel.get_abs_rect().width, 130),
            manager=self.manager,
            container=self.panel,
            object_id="#panelButton",
            anchors={"centerx": "centerx", "top": "top"},
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