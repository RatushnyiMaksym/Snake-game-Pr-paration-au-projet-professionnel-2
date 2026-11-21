import pygame


class Map:
    """
    Gère la grille, les dimensions, les règles de bordure et les obstacles
    en fonction du map_id choisi.
    """

    def __init__(self, map_id, cell_size=20):
        self.map_id = map_id
        self.cell_size = cell_size

        # Configuration des différentes cartes selon le map_id (1 à 4)
        if map_id == 1:
            # Carte 1 : Classique ouverte (les bords traversent)
            self.width = 20  # Nombre de colonnes (cases)
            self.height = 20  # Nombre de lignes (cases)
            self.wraps = True
            self.obstacles = set()

        elif map_id == 2:
            # Carte 2 : Fermée (les murs tuent le serpent)
            self.width = 20
            self.height = 20
            self.wraps = False
            self.obstacles = set()

        elif map_id == 3:
            # Carte 3 : 25x25 fermée avec obstacles loin du centre (12, 12)
            self.width = 25
            self.height = 25
            self.wraps = False
            self.obstacles = {
                # Bloc supérieur gauche
                (4, 4), (5, 4), (6, 4),
                (4, 5), (4, 6),
                # Bloc supérieur droit
                (18, 4), (19, 4), (20, 4),
                (20, 5), (20, 6),
                # Bloc inférieur gauche
                (4, 18), (4, 19), (4, 20),
                (5, 20), (6, 20),
                # Bloc inférieur droit
                (20, 18), (20, 19), (20, 20),
                (18, 20), (19, 20),
            }

        elif map_id == 4:
            # Carte 4 : 24x24 traversante avec piliers espacés
            self.width = 24
            self.height = 24
            self.wraps = True
            self.obstacles = {
                (6, 6), (7, 6), (6, 7),
                (16, 6), (17, 6), (17, 7),
                (6, 16), (6, 17), (7, 17),
                (16, 17), (17, 16), (17, 17),
            }
        else:
            raise ValueError("Map ID invalide (doit être entre 1 et 4).")



    def get_width(self):
        """Retourne la largeur de la carte en nombre de cases."""
        return self.width

    def get_height(self):
        """Retourne la hauteur de la carte en nombre de cases."""
        return self.height

    def get_cell_size(self):
        """Retourne la taille d'une case en pixels."""
        return self.cell_size
        
    def wraps_edges(self):
        """Retourne True si le serpent traverse les bords, False sinon."""
        return self.wraps

    def is_obstacle(self, position):
        """Vérifie si une position (x, y en cases) contient un obstacle."""
        return position in self.obstacles

    def get_center(self):
        """Retourne les coordonnées centrales de la carte pour faire spawn le serpent."""
        return (self.width // 2, self.height // 2)

    
    # Affichage (pygame)
    

    def draw(self, screen):
        """Dessine le fond de la carte, la grille et les obstacles."""

        # 1. Remplir le fond de la fenêtre
        screen.fill((20, 20, 20))

        # 2. Dessiner une grille visuelle discrète
        window_width = self.width * self.cell_size
        window_height = self.height * self.cell_size

        for x in range(0, window_width, self.cell_size):
            for y in range(0, window_height, self.cell_size):
                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, (30, 30, 30), rect, 1)  # Ligne grise fine

        # 3. Dessiner les obstacles s'il y en a
        for obs_x, obs_y in self.obstacles:
            obstacle_rect = pygame.Rect(
                obs_x * self.cell_size,
                obs_y * self.cell_size,
                self.cell_size,
                self.cell_size
            )
            pygame.draw.rect(screen, (100, 100, 100), obstacle_rect)  # Gris clair pour les murs
