"""
model.py

Contient les principaux objets et règles du jeu Snake.

Responsabilités :
- Représenter l'état d'une partie.
- Gérer le serpent.
- Gérer le fruit.
- Gérer les déplacements.
- Gérer les collisions.
- Gérer le score.
- Appliquer les règles liées à la carte et à la difficulté.

Ce fichier ne doit pas gérer :
- l'affichage de l'interface ;
- les requêtes HTTP ;
- les routes de l'application ;
- les éléments HTML/CSS/JavaScript.

Ces responsabilités appartiennent respectivement au frontend
et au controller.py.
"""

from maps import MAP_WIDTH, MAP_HEIGHT, get_map


class Snake:
    """
    Représente le serpent du joueur.

    Le serpent est représenté par une liste de positions.
    Le premier élément de la liste représente toujours la tête.
    Le dernier élément représente la queue.
    """

    def __init__(self, start_position):
        """
        Crée un nouveau serpent.

        Args:
            start_position: Position initiale de la tête du serpent.

        Le serpent doit commencer avec la longueur initiale
        définie par les règles du jeu.

        La direction initiale doit être nulle :
        le serpent ne se déplace pas avant la première
        commande du joueur.
        """
        pass

    def set_direction(self, direction):
        """
        Définit la direction du serpent.

        Args:
            direction: Nouvelle direction demandée.

        La direction doit être refusée si elle constitue
        un demi-tour immédiat par rapport à la direction actuelle.

        La validation de la direction doit respecter les règles
        du jeu.
        """
        pass

    def get_next_position(self):
        """
        Calcule la prochaine position de la tête du serpent.

        La position est calculée à partir de la position actuelle
        de la tête et de la direction actuelle.

        Cette méthode ne doit pas modifier le serpent.

        Returns:
            La position que la tête occuperait au prochain déplacement.
        """
        pass

    def move(self, new_position, grow=False):
        """
        Déplace le serpent vers une nouvelle position.

        Args:
            new_position: Nouvelle position de la tête.
            grow: Indique si le serpent doit conserver un segment
                  supplémentaire après le déplacement.

        Le déplacement doit mettre à jour les positions
        de tous les segments du serpent.
        """
        pass

    def get_head(self):
        """
        Retourne la position actuelle de la tête du serpent.

        Returns:
            La première position de la liste représentant le serpent.
        """
        pass

    def get_body(self):
        """
        Retourne les positions occupées par le corps du serpent.

        La tête n'est pas incluse dans le résultat.
        """
        pass

    def get_length(self):
        """
        Retourne la longueur actuelle du serpent.

        La longueur doit être déterminée à partir des positions
        actuellement occupées par le serpent.
        """
        pass


class Fruit:
    """
    Représente un fruit présent sur la carte.
    """

    def __init__(self, position, points):
        """
        Crée un fruit.

        Args:
            position: Position du fruit sur la carte.
            points: Nombre de points accordés lorsque le fruit est mangé.
        """
        pass

    def get_position(self):
        """
        Retourne la position actuelle du fruit.

        Returns:
            Position du fruit.
        """
        pass

    def get_points(self):
        """
        Retourne la valeur du fruit.

        Returns:
            Nombre de points accordés lorsque le fruit est mangé.
        """
        pass


class Game:
    """
    Représente une partie complète de Snake.

    La configuration de la partie est définie lors de sa création
    et ne change pas pendant la partie.

    Configuration :
    - difficulté ;
    - carte.

    État dynamique :
    - serpent ;
    - direction ;
    - fruit ;
    - score ;
    - statut de la partie.
    """

    def __init__(self, difficulty, map_id):
        """
        Crée une nouvelle partie.

        Args:
            difficulty: Niveau de difficulté entre 1 et 4.
            map_id: Numéro de la carte entre 1 et 4.

        La partie doit être initialisée avec :
        - la carte sélectionnée ;
        - un serpent au centre de la carte ;
        - aucun déplacement initial ;
        - un score de zéro ;
        - un fruit placé sur une position valide ;
        - le statut 'waiting'.

        La difficulté et la carte doivent être conservées
        comme configuration de cette partie.
        """
        pass

    def change_direction(self, direction):
        """
        Demande un changement de direction du serpent.

        Args:
            direction: Nouvelle direction demandée.

        La direction doit respecter les règles du serpent,
        notamment l'interdiction du demi-tour immédiat.

        Si la partie est encore dans l'état 'waiting',
        la première direction valide doit faire passer
        la partie à l'état 'running'.
        """
        pass

    def update(self):
        """
        Effectue une étape de la logique du jeu.

        Cette méthode doit notamment :
        - déterminer la prochaine position du serpent ;
        - appliquer les règles de la carte ;
        - vérifier les collisions ;
        - déplacer le serpent ;
        - vérifier si un fruit est mangé ;
        - mettre à jour le score et la longueur du serpent ;
        - générer un nouveau fruit si nécessaire.

        La méthode ne doit pas gérer l'affichage.
        """
        pass

    def check_collision(self, position):
        """
        Vérifie si une position provoque une collision.

        Args:
            position: Position à vérifier.

        Les collisions possibles sont :
        - collision avec le corps du serpent ;
        - collision avec une bordure ;
        - collision avec un obstacle.

        Le comportement des bordures dépend de la carte utilisée.

        Returns:
            True si la position provoque une collision,
            False sinon.
        """
        pass

    def handle_map_boundaries(self, position):
        """
        Applique les règles de bordure de la carte.

        Pour une carte avec passage libre, une position
        dépassant une bordure est replacée de l'autre côté.

        Pour une carte avec bordures, une position située
        hors de la carte provoque une collision.

        Args:
            position: Position à vérifier.

        Returns:
            La nouvelle position si le passage est autorisé.
            None si la position provoque une collision.
        """
        pass

    def is_fruit_eaten(self):
        """
        Vérifie si la tête du serpent se trouve sur le fruit actuel.

        Returns:
            True si le fruit est mangé, False sinon.
        """
        pass

    def eat_fruit(self):
        """
        Gère la consommation du fruit actuel.

        Cette méthode doit :
        - augmenter le score ;
        - faire grandir le serpent ;
        - générer un nouveau fruit.

        La valeur du fruit dépend de la difficulté
        configurée pour la partie.
        """
        pass

    def generate_fruit(self):
        """
        Génère un nouveau fruit sur une position valide.

        Le fruit ne doit pas apparaître :
        - sur le serpent ;
        - sur un obstacle ;
        - sur une position invalide de la carte.

        La méthode doit continuer à chercher une position
        jusqu'à ce qu'une position valide soit trouvée.
        """
        pass

    def is_game_over(self):
        """
        Vérifie si la partie est terminée.

        Returns:
            True si la partie est terminée, False sinon.
        """
        pass

    def end_game(self):
        """
        Termine la partie.

        Le statut de la partie doit passer à 'game_over'
        et le déplacement du serpent doit s'arrêter.
        """
        pass

    def reset(self):
        """
        Réinitialise la partie.

        Le serpent, le score, la direction et le fruit
        doivent retrouver leur état initial.

        La difficulté et la carte sélectionnées sont conservées.
        """
        pass

    def get_state(self):
        """
        Retourne l'état dynamique actuel de la partie.

        L'état doit contenir uniquement les informations
        nécessaires pour représenter l'état actuel du jeu.

        Il doit notamment contenir :
        - les positions du serpent ;
        - la direction ;
        - la position du fruit ;
        - le score ;
        - le statut de la partie.

        La difficulté et la carte ne font pas partie
        de cet état dynamique.
        """
        pass