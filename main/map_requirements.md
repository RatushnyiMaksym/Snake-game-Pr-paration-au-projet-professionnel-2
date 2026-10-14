# Documentation du Module `Map`

Ce document décrit le rôle, les caractéristiques et l'interface attendue pour le module `Map` dans le projet Snake.

---

## 1. Rôle du module
La classe `Map` est responsable de :
- Gérer la taille de l'aire de jeu (en nombre de cases).
- Définir le comportement des bordures (si le serpent traverse ou s'il meurt en touchant les murs).
- Gérer les obstacles internes selon le niveau choisi (`map_id`).
- Dessiner la grille, le fond et les obstacles à l'écran via Pygame.

---

## 2. Interface Requise (Contrat avec `Game`)

Le module doit exposer les méthodes suivantes pour que le contrôleur de jeu (`Game`) puisse interagir avec lui :

### `map.get_width()`
- **Retour :** `int`
- **Description :** Retourne la largeur de la carte en nombre de cases.

### `map.get_height()`
- **Retour :** `int`
- **Description :** Retourne la hauteur de la carte en nombre de cases.

### `map.wraps_edges()`
- **Retour :** `bool`
- **Description :** 
  - `True` si le serpent traverse les bords pour réapparaître de l'autre côté.
  - `False` si sortir de la carte provoque une collision (Game Over).

### `map.is_obstacle(position)`
- **Paramètre :** `position` (tuple `(x, y)` en coordonnées de grille)
- **Retour :** `bool`
- **Description :** Retourne `True` si la case correspond à un obstacle fixe, sinon `False`.

### `map.get_center()`
- **Retour :** tuple `(x, y)` en coordonnées de grille
- **Description :** Retourne les coordonnées du centre de la carte (utilisé pour faire spawner le serpent au début de la partie).

### `map.draw(screen)`
- **Paramètre :** `screen` (la surface Pygame principale)
- **Description :** Dessine le fond de la carte, la grille visuelle et les obstacles éventuels.

---

## 3. Spécifications des Cartes (`map_id`)

Le jeu propose 4 configurations de cartes différentes identifiées par un entier de `1` à `4` :

| Map ID | Type de bordure (`wraps_edges`) | Dimensions (Colonnes x Lignes) | Obstacles internes |
| :---: | :---: | :---: | :--- |
| **1** | `True` (Traversant) | $20 \times 20$ | Aucun |
| **2** | `False` (Fermé / Mortel) | $20 \times 20$ | Aucun |
| **3** | `False` (Fermé / Mortel) | $25 \times 25$ | Présence de murs internes fixes |
| **4** | `True` (Traversant) | $30 \times 20$ | Présence de blocs d'obstacles |

---

## 4. Conventions techniques
- **Système de coordonnées :** Toutes les positions et les obstacles internes sont stockés en **coordonnées de grille** `(x, y)`.
- **Conversion en pixels :** La conversion en pixels (via la taille d'une case `cell_size`) est effectuée uniquement à l'intérieur de la méthode de dessin (`draw`).
- **Représentation des obstacles :** Les obstacles internes doivent être stockés dans une structure optimisée pour la recherche (par exemple un `set` de tuples `{(x, y), ...}`).
