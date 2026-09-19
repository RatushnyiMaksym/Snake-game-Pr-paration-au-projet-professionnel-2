"""
controller.py

Gère les requêtes de l'application web et fait le lien
entre le frontend et le modèle du jeu.

Responsabilités :
- Recevoir les requêtes du frontend.
- Appeler les méthodes appropriées du modèle.
- Retourner les données nécessaires au frontend.
- Gérer les entrées utilisateur liées au jeu.

Ce fichier ne doit pas contenir :
- la logique principale du jeu ;
- les règles de déplacement ;
- les règles de collision ;
- la logique de score ;
- la génération des fruits ;
- le code HTML/CSS/JavaScript.

Ces responsabilités appartiennent au modèle et au frontend.
"""

from model import Game


# Référence vers la partie actuellement en cours.
# Le backend peut choisir une autre manière de gérer
# cette référence si nécessaire.
game = None


def start_game(difficulty, map_id):
    """
    Crée une nouvelle partie.

    Args:
        difficulty: Niveau de difficulté choisi par le joueur.
        map_id: Carte choisie par le joueur.

    Cette fonction doit :
    - créer une nouvelle instance de Game ;
    - conserver cette partie comme partie actuelle ;
    - retourner les informations nécessaires
      au frontend.

    Returns:
        L'état initial de la partie.
    """
    pass


def get_game_state():
    """
    Retourne l'état actuel de la partie.

    Cette fonction doit récupérer l'état depuis le modèle
    et le transmettre au frontend.

    Returns:
        L'état dynamique actuel de la partie.
    """
    pass


def change_direction(direction):
    """
    Transmet une nouvelle direction au modèle.

    Args:
        direction: Direction demandée par le joueur.

    La validation de la direction est effectuée
    par le modèle et non par le contrôleur.

    Returns:
        Le résultat de la demande de changement de direction.
    """
    pass


def update_game():
    """
    Demande au modèle d'effectuer une étape du jeu.

    Le contrôleur ne décide pas :
    - de la prochaine position ;
    - des collisions ;
    - de la croissance du serpent ;
    - du score.

    Ces décisions appartiennent au modèle.

    Returns:
        Le nouvel état de la partie après la mise à jour.
    """
    pass


def end_game():
    """
    Termine la partie actuelle.

    Cette fonction demande au modèle de terminer
    la partie en cours.

    Returns:
        L'état final de la partie.
    """
    pass


def reset_game():
    """
    Réinitialise la partie actuelle.

    La difficulté et la carte sélectionnées
    doivent être conservées.

    Returns:
        L'état de la partie après réinitialisation.
    """
    pass


def get_scoreboard():
    """
    Retourne le classement actuel des scores.

    Le classement est conservé uniquement pendant
    la session de l'application.

    Returns:
        Les 10 meilleurs scores enregistrés.
    """
    pass