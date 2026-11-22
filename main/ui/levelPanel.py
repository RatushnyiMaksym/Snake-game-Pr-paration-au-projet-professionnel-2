import pygame
import pygame_gui
from map import Map
from utils.buttonMaker import make_button
from utils.placeHolderMaker import makePlaceholder


NB_CARDS = 4
BTN_W, BTN_GAP = 247, 30
MIN_DIFFICULTY, MAX_DIFFICULTY = 1, 3





class LevelPanel:
    def __init__(self, manager, win):
        self.manager = manager
        self.win = win
        w, h = self.win.screen.get_size()


        self.panelPseudo = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(20, -50, 260, 200),
            manager=self.manager,
            object_id="#pseudoPanel",
            anchors={"left": "left", "centery": "centery"},
        )
        self.pseudoLabel = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, 20, 220, 50),
            text="Player name",
            manager=self.manager,
            container=self.panelPseudo,
            anchors={"centerx": "centerx", "top": "top"},
        )
        self.pseudoEntry = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(0, 85, 220, 45),
            manager=self.manager,
            container=self.panelPseudo,
            anchors={"centerx": "centerx", "top": "top"},
        )
        self.pseudoEntry.set_text_length_limit(16)


        self.panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(20, -50, w - 300 - 20, 820),
            manager=self.manager,
            object_id="#levelPanel",
            anchors={"left": "left", "left_target": self.panelPseudo, "centery": "centery"},
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
            text="Choose your level",
            manager=self.manager,
            container=self.panelTitle,
            object_id="#title",
            anchors={"center": "center"},
        )


        self.panelCards = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(0, 170, wP, 400),
            manager=self.manager,
            container=self.panel,
            object_id="#panelCards",
            anchors={"centerx": "centerx", "top": "top"},
        )
        gap = 20
        card = min(200, (wP - (NB_CARDS + 1) * gap) // NB_CARDS)
        margin = (wP - (NB_CARDS * card + (NB_CARDS - 1) * gap)) // 2
        self.cardImages, self.cardLabels, self.cardButtons = [], [], []
        for i in range(NB_CARDS):
            x = margin + i * (card + gap)
            image = pygame_gui.elements.UIImage(
                relative_rect=pygame.Rect(x, 20, card, card),
                image_surface=makePlaceholder(card),
                manager=self.manager,
                container=self.panelCards,
            )
            label = pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect(x, 20 + card + 5, card, 50),
                text=f"Map {i + 1}",
                manager=self.manager,
                container=self.panelCards,
            )
            button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(x, 20, card, card + 55),
                text="",
                manager=self.manager,
                container=self.panelCards,
                object_id="#cardButton",
            )

            self.cardImages.append(image)
            self.cardLabels.append(label)
            self.cardButtons.append(button)
        self.selectMap(0)


        yDiff = 20 + card + 5 + 50 + 30
        self.difficultyLabel = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(-60, yDiff, 220, 50),
            text="Level difficulty",
            manager=self.manager,
            container=self.panelCards,
            anchors={"centerx": "centerx", "top": "top"},
        )
        self.difficultyEntry = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(120, yDiff + 2, 100, 45),
            manager=self.manager,
            container=self.panelCards,
            anchors={"centerx": "centerx", "top": "top"},
        )
        self.difficultyEntry.set_allowed_characters("numbers")
        self.difficultyEntry.set_text_length_limit(1)
        self.difficultyEntry.set_text(str(MIN_DIFFICULTY))


        self.panelButton = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(0, 590, wP, 130),
            manager=self.manager,
            container=self.panel,
            object_id="#panelButton",
            anchors={"centerx": "centerx", "top": "top"},
        )
        offset = (BTN_W + BTN_GAP) // 2
        y = (130 - 81) // 2
        self.back_button = make_button("←", -offset, y, self.manager, panel=self.panelButton,object_id="#backButton")
        self.go_button = make_button("Start", offset, y, self.manager, panel=self.panelButton)

    def selectMap(self, index):
        self.selectedMap = index
        for i, button in enumerate(self.cardButtons):
            if i == index:
                button.select()
            else:
                button.unselect()

    def getPseudo(self):
        return self.pseudoEntry.get_text().strip()

    def getDifficulty(self):
        text = self.difficultyEntry.get_text()
        value = int(text) if text else MIN_DIFFICULTY
        return max(MIN_DIFFICULTY, min(MAX_DIFFICULTY, value))


    def show(self):
        self.panelPseudo.show()
        self.panel.show()

    def kill(self):
        self.panelPseudo.kill()
        self.panel.kill()

    def handleEvent(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element in self.cardButtons:
                self.selectMap(self.cardButtons.index(event.ui_element))
            match event.ui_element:
                case self.back_button:
                    self.win.navigationPanel("home")
                case self.go_button:
                    print("Start :", self.getPseudo() or "(sans pseudo)", "| difficulte", self.getDifficulty())
                    self.win.navigationPanel("start")
        elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
            if event.ui_element == self.difficultyEntry:
                self.difficultyEntry.set_text(str(self.getDifficulty()))