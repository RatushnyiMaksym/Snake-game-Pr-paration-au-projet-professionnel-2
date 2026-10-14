# Snake — Interfaces et requirements

## 1. Représentation des positions

- Toutes les positions sont représentées par des tuples `(x, y)` en coordonnées de grille.
- La tête du serpent est toujours le premier élément de `body` : `body[0]`.
- La queue est le dernier élément : `body[-1]`.
- La conversion des coordonnées de grille en pixels est effectuée uniquement lors de l'affichage.

## 2. Initialisation

```python
snake = Snake(start_x, start_y, initial_length=3, cell_size=20)
```

- `start_x`, `start_y` : position initiale de la tête.
- `initial_length` : longueur initiale du serpent, fixée par défaut à 3 cases.
- `cell_size` : taille d'une case en pixels, fixée par défaut à 20.
- La direction initiale est `None` : le serpent ne se déplace pas tant qu'une direction n'a pas été définie.

Pour une grille de 30 × 20 cases, la fenêtre de jeu correspond à 600 × 400 pixels si chaque case mesure 20 × 20 pixels.

## 3. Méthodes disponibles

| Méthode | Utilité |
|---|---|
| `get_head()` | Retourne la position de la tête `(x, y)`. |
| `get_body()` | Retourne une copie de la liste des positions du serpent. |
| `change_direction(new_direction)` | Change la direction sans autoriser un demi-tour immédiat. |
| `move(position, grow=False)` | Déplace le serpent vers la position fournie. |
| `has_self_collision()` | Vérifie si la tête chevauche le reste du corps. |
| `draw(screen)` | Dessine le serpent avec Pygame. |

## 4. Déplacement et croissance

La méthode `move(position, grow=False)` reçoit la prochaine position de la tête calculée par `Game`.

- `grow=False` : la nouvelle tête est ajoutée et la queue est supprimée.
- `grow=True` : la nouvelle tête est ajoutée et la queue est conservée, ce qui augmente la longueur d'un segment.

`Game` est responsable de vérifier les collisions avec la carte et de détecter si le serpent mange un fruit avant de confirmer son déplacement.

## 5. Affichage

La méthode `draw(screen)` utilise la taille de case enregistrée lors de l'initialisation du serpent. Elle reçoit la fenêtre Pygame et dessine la tête et le corps à partir des coordonnées de grille.

## 6. Exemple d'utilisation dans `game.py`

```python
from snake import Snake

snake = Snake(10, 5, initial_length=3, cell_size=20)

head = snake.get_head()
body = snake.get_body()

snake.change_direction((1, 0))

# Exemple : Game calcule la prochaine position.
next_position = (head[0] + 1, head[1])

# Game vérifie les collisions et détermine si un fruit est mangé.
snake.move(next_position, grow=False)

snake.draw(screen)
```

**Remarque :** `screen` doit être une fenêtre Pygame initialisée par `Game`. L'exemple suppose que la prochaine position a déjà été validée par la logique du jeu.
