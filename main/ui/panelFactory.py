

from ui.homePanel import HomePanel
from ui.infosPanel import InfosPanel
from ui.levelPanel import LevelPanel
from ui.settingsPanel import SettingsPanel
from ui.gamePanel import GamePanel

class PanelFactory:
    def __init__(self,manager,win):
        self.manager = manager
        self.win = win


    def createPanel(self,panelType):
        panel = None
        match panelType:
            case "home":
               panel= HomePanel(self.manager,self.win)
            case "infos":
              panel =  InfosPanel(self.manager,self.win)
            case "settings":
                panel = SettingsPanel(self.manager,self.win)
            case "level":
                panel = LevelPanel(self.manager,self.win)
            case "start":
                panel = GamePanel(self.manager,self.win)
            case _:
                raise ValueError("Panel type non existing")


        panel.show()
        return panel