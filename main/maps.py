"""
maps.py

Contient les définitions des cartes du jeu Snake.

Toutes les cartes utilisent les mêmes dimensions.

Responsabilités :
- Définir les dimensions communes des cartes.
- Définir les obstacles de chaque carte.
- Définir le comportement des bordures.
- Fournir la carte demandée au modèle.

Ce fichier ne contient pas la logique du jeu.
"""


# Dimensions communes à toutes les cartes.
MAP_WIDTH = 20 # par example
MAP_HEIGHT = 15 # par example


# Définitions des cartes.
#
# obstacles : positions occupées par des obstacles.

MAPS = {
    
}


def get_map(map_id):
    """
    Retourne la définition d'une carte.

    Args:
        map_id: Numéro de la carte entre 1 et 4.

    Returns:
        Les informations de la carte sélectionnée.
    """
    pass