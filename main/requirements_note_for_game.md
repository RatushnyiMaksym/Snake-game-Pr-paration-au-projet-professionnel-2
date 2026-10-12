# Interfaces nécessaires pour le module `Game`

Le fichier `game.py` est responsable de la coordination générale de la partie.  
Pour pouvoir communiquer avec les modules `Snake`, `Map` et `Fruit`, merci de fournir les informations/méthodes suivantes.

L'objectif est de définir **ce que `Game` peut utiliser**, sans imposer la manière dont chaque module est implémenté.

---

## 1. Module `Snake`

### Informations nécessaires

`Game` doit pouvoir :

- connaître la position de la tête ;
- connaître toutes les positions occupées par le serpent ;
- déplacer le serpent ;
- augmenter sa longueur ;
- éventuellement le dessiner avec Pygame.

### Interface souhaitée

```python
snake.get_head()
```

Retourne la position de la tête :

```python
(x, y)
```

---

```python
snake.get_body()
```

Retourne la liste des positions occupées par le serpent, avec la tête en première position :

```python
[
    (x_head, y_head),
    (x1, y1),
    (x2, y2),
    ...
]
```

---

```python
snake.move(position, grow=False)
```

Déplace le serpent vers `position`.

- `grow=False` → déplacement normal, la queue est supprimée ;
- `grow=True` → le serpent conserve sa queue et gagne donc un segment.

Exemple :

```python
snake.move((6, 4))
```

ou :

```python
snake.move((6, 4), grow=True)
```

---

```python
snake.draw(screen)
```

Dessine le serpent avec Pygame.

---

### À préciser

Merci de confirmer :

- la représentation utilisée pour une position : `(x, y)`, `pygame.Rect`, autre ;
- la position initiale attendue lors de la création du serpent ;
- la longueur initiale ;
- si `move()` calcule lui-même la nouvelle position ou si `Game` lui fournit la position ;
- comment le serpent est initialisé/réinitialisé.

---

# 2. Module `Map`

### Informations nécessaires

`Game` doit pouvoir :

- connaître les dimensions de la carte ;
- savoir si les bords permettent le passage d'un côté à l'autre ;
- savoir si une position correspond à un obstacle ;
- éventuellement dessiner la carte.

### Interface souhaitée

```python
map.get_width()
```

Retourne la largeur de la carte en cases.

---

```python
map.get_height()
```

Retourne la hauteur de la carte en cases.

---

```python
map.wraps_edges()
```

Retourne :

```python
True
```

si le serpent doit réapparaître de l'autre côté lorsqu'il sort de la carte.

Retourne :

```python
False
```

si sortir de la carte provoque une collision.

---

```python
map.is_obstacle(position)
```

Retourne `True` si la position correspond à un obstacle.

Exemple :

```python
map.is_obstacle((5, 4))
```

---

```python
map.draw(screen)
```

Dessine la carte, les bordures et les obstacles avec Pygame.

---

### À préciser

Merci de confirmer :

- les dimensions communes des cartes ;
- la représentation des obstacles ;
- comment les quatre cartes sont identifiées ;
- comment une carte est créée/sélectionnée ;
- si les bordures sont incluses dans les obstacles ou gérées séparément ;
- comment la carte est réinitialisée.

---

# 3. Module `Fruit`

### Informations nécessaires

`Game` doit pouvoir :

- connaître la position du fruit ;
- générer/repositionner un fruit ;
- dessiner le fruit.

La génération doit tenir compte de la carte et des positions occupées par le serpent.

### Interface souhaitée

```python
fruit.get_position()
```

Retourne la position actuelle du fruit :

```python
(x, y)
```

---

```python
fruit.spawn(map, occupied_positions)
```

Génère un nouveau fruit sur une position valide.

Le fruit ne doit pas apparaître :

- sur le serpent ;
- sur un obstacle ;
- hors de la carte.

`occupied_positions` peut par exemple être :

```python
snake.get_body()
```

---

```python
fruit.draw(screen)
```

Dessine le fruit avec Pygame.

---

### À préciser

Merci de confirmer :

- la représentation utilisée pour la position du fruit ;
- comment le fruit est initialisé ;
- comment une position libre est recherchée ;
- si `Fruit` reçoit directement la carte ou uniquement ses dimensions/obstacles ;
- comment le fruit est réinitialisé.

---

# 4. Convention commune pour les positions

Pour simplifier l'intégration, je propose que **tous les modules utilisent des coordonnées de grille** et non des coordonnées en pixels.

Exemple :

```python
(0, 0)
(1, 0)
(2, 0)
(2, 1)
```

Le passage des coordonnées de grille vers les pixels Pygame serait effectué uniquement lors du dessin.

Par exemple :

```python
pixel_x = grid_x * CELL_SIZE
pixel_y = grid_y * CELL_SIZE
```

Cela permet d'utiliser les mêmes coordonnées pour :

- le serpent ;
- les fruits ;
- les obstacles ;
- les collisions ;
- les déplacements.

---

# 5. Résumé des interfaces

| Module | Méthode | Utilité |
|---|---|---|
| Snake | `get_head()` | Position de la tête |
| Snake | `get_body()` | Positions de tout le serpent |
| Snake | `move(position, grow)` | Déplacer / faire grandir |
| Snake | `draw(screen)` | Afficher le serpent |
| Map | `get_width()` | Largeur en cases |
| Map | `get_height()` | Hauteur en cases |
| Map | `wraps_edges()` | Passage libre ou collision aux bords |
| Map | `is_obstacle(position)` | Vérifier un obstacle |
| Map | `draw(screen)` | Afficher la carte |
| Fruit | `get_position()` | Position du fruit |
| Fruit | `spawn(map, occupied_positions)` | Générer un nouveau fruit |
| Fruit | `draw(screen)` | Afficher le fruit |

**Les noms des méthodes peuvent être modifiés si vous avez déjà une convention différente. L'important est que `Game` puisse obtenir ces informations et effectuer ces opérations.**