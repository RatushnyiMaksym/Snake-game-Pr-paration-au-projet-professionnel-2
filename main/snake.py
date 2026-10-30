import pygame

# Créer le serpent
class Snake:
    def __init__(self, start_x, start_y, initial_length=3, cell_size=20):

        # contient les positions de tous les segments (self.body[0] : tête, self.body[-1] : queue)
        self.body = [(start_x - i, start_y) # position initiale du serpent
        for i in range(initial_length)]

        self.direction = None       # serpent ne bouge pas encore
        self.cell_size = cell_size    # cell_size : taille en pixels d'une case

    # position de la tête    
    def get_head(self): # retourne la position de la tête
        return self.body[0]

    # copie de la liste
    def get_body(self): # retourne les positions de tous les segments
        return self.body.copy()

    # retourne la direction actuelle du serpent
    def get_direction(self):
        return self.direction
    
    # changement de direction
    def change_direction(self, new_direction):
        # change de direction sans permettre un demi-tour
        if new_direction not in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            return False
        
        if self.direction is None:
            self.direction = new_direction
            return True

        opposite = (-self.direction[0], -self.direction[1]) # les positions opposées

        # si on a la direction opposée, on accepte le changement
        if new_direction == opposite:
            return False

        self.direction = new_direction
        return True

    # déplacer le serpent (Game vérifie les collisions)
    def move(self, position, grow=False):   # agrandir le serpent (conserve la queue et ajoute un segment)
        
        self.body.insert(0, position)   # récupérer la position du serpent

        if not grow:
            self.body.pop()

    def has_self_collision(self):   # si la tête touche le corps
        return self.body[0] in self.body[1:]

    # dessiner le serpent
    def draw(self, screen): # screen : fenêtre crée dans Game
         
         for index, (x, y) in enumerate(self.body):
            # rectangle (longueur et hauteur)
            rect = (
                x * self.cell_size,
                y * self.cell_size,
                self.cell_size,
                self.cell_size
            )

            # Tête plus claire que le reste du corps
            color = (0, 255, 0) if index == 0 else (0, 180, 0)
            pygame.draw.rect(screen, color, rect)

