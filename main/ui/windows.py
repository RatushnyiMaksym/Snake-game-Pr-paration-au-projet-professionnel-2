from ui.panelFactory import PanelFactory

import pygame
import pygame_gui

class Windows:

    def __init__(self):
        self.windowSize = (1000, 900)
        self.manager = pygame_gui.UIManager(self.windowSize, "main/static/Theme.json")
        self.bgColor = (148, 193, 209)
        self.grassHeight = 110
        self.screen = pygame.display.set_mode(self.windowSize, pygame.RESIZABLE)
        pygame.display.set_caption("Snake Game")
        self.currentPanel = PanelFactory(self.manager, self).createPanel("home")
        self.clock = pygame.time.Clock()
        self.running = False

        self.grass = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(0, -self.grassHeight, self.windowSize[0], self.grassHeight),
            manager=self.manager,
            object_id="#grass",
            anchors={"left": "left", "right": "right", "bottom": "bottom"},
        )
        APPLE_SIZE = 52
        
        apple_surface = pygame.image.load_sized_svg("main/static/images/svg/apple.svg", (APPLE_SIZE, APPLE_SIZE))
        self.apple = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect(-APPLE_SIZE - 60, -self.grassHeight - APPLE_SIZE + 3, APPLE_SIZE, APPLE_SIZE),
            image_surface=apple_surface,
            manager=self.manager,
            anchors={"right": "right", "bottom": "bottom"},
        )



    def run(self):
        self.running = True
        while self.running:
            time = self.clock.tick(60) / 1000

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.running = False
                elif ev.type == pygame.VIDEORESIZE:
                    self.manager.set_window_resolution(ev.size)

                self.manager.process_events(ev)
                self.currentPanel.handleEvent(ev)
            self.manager.update(time)
            self.screen.fill(self.bgColor)
            self.manager.draw_ui(self.screen)
            pygame.display.update()
            self.manager.set_visual_debug_mode(True)
        pygame.quit()


    def navigationPanel(self, type="home"):
        self.currentPanel.kill()
        self.currentPanel = PanelFactory(self.manager, self).createPanel(type)
