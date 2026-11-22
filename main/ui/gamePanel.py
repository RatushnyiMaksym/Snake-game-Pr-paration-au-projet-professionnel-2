import pygame
import pygame_gui
from utils.buttonMaker import make_button

class GamePanel:
    def __init__(self, manager, win):
        self.manager = manager
        self.win = win
        # pour un chrono
        self.start_time = pygame.time.get_ticks()
        self.TIMER_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.TIMER_EVENT, 100)

        w, h = self.win.screen.get_size()

        self.panelScore = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(20, -50, 260, 200),
            manager=self.manager,
            object_id="#scorePanel",
            anchors={"left": "left", "centery": "centery"},
        )
        self.scoreLabel = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, 0, 220, 50),
            text="Score : 0",
            manager=self.manager,
            container=self.panelScore,
            anchors={"centerx": "centerx", "top": "top"},

        )

        self.timeLabel = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, 30, 220, 50),
            text=f"Time : 00:00",
            manager=self.manager,
            container=self.panelScore,
            anchors={"centerx": "centerx", "top_target": self.scoreLabel},

        )

        self.panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(20, -50, w - 300 - 20, 820),
            manager=self.manager,
            object_id="#GamePanel",
            anchors={"left": "left", "left_target": self.panelScore, "centery": "centery"},
        )
        wP = self.panel.get_abs_rect().width

        self.panelTitle = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(0, 0, wP, 160),
            manager=self.manager,
            container=self.panel,
            object_id="#panelTitle",
            anchors={"centerx": "centerx", "top": "top"},
        )
        self.titleLabel = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, 0, wP, 160),
            text="Good luck !",
            manager=self.manager,
            container=self.panelTitle,
            object_id="#title",
            anchors={"center": "center"},
        )

        self.panelMap = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(0, 170, 500, 500),
            manager=self.manager,
            container=self.panel,
            object_id="#panelMap",
            anchors={"centerx": "centerx", "top": "top"},
        )
        self.panelButton = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(0, 690, wP, 130),
            manager=self.manager,
            container=self.panel,
            object_id="#panelButton",
            anchors={"centerx": "centerx", "top": "top"},
        )

        self.back_button = make_button("←", 0, 0, self.manager, panel=self.panelButton, object_id="#backButton")

    def update_timer(self):
        if self.timer_running:
            self.elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000

        minutes = self.elapsed_time // 60
        secondes = self.elapsed_time % 60

        self.timeLabel.set_text(f"Time : {minutes:02}:{secondes:02}")

    def stop_timer(self):
        self.elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
        self.timer_running = False

    def show(self):
        self.panelScore.show()
        self.panel.show()

    def kill(self):
        pygame.time.set_timer(self.TIMER_EVENT, 0)
        self.panelScore.kill()
        self.panel.kill()


    def handleEvent(self, event):

        if event.type == self.TIMER_EVENT:
            elapsed = (pygame.time.get_ticks() - self.start_time) // 1000

            minutes = elapsed // 60
            secondes = elapsed % 60

            self.timeLabel.set_text(f"Time : {minutes:02}:{secondes:02}")

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if getattr(event, "ui_element", None) == self.back_button:
                pygame.time.set_timer(self.TIMER_EVENT, 0)
                self.win.navigationPanel("level")