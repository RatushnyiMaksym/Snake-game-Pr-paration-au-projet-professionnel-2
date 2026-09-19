# Logique du jeu — Snake

## 1. Organisation des données

La logique du jeu distingue la **configuration de la partie** de son **état dynamique**.

**### Configuration**

La configuration est définie au lancement :

* difficulté ;
* carte sélectionnée.

La difficulté est associée à l'instance de `Game`.

Les définitions des cartes sont centralisées dans `maps.py`.

`maps.py` contient notamment :

* les dimensions communes des cartes ;
* les obstacles de chaque carte ;
* le comportement des bordures ;
* l'identifiant et le nom de chaque carte.

Exemple conceptuel :

```python
game = Game(
    difficulty=2,
    map_id=3
)
```

Le `Game` utilise `map_id` pour récupérer la définition correspondante dans `maps.py`.

La configuration sélectionnée ne change pas pendant une partie.

**### Définition des cartes**

Toutes les cartes utilisent les mêmes dimensions rectangulaires.

Les cartes sont identifiées par un numéro :

```text
1 → carte 1
2 → carte 2
3 → carte 3
4 → carte 4
```

Les obstacles et les règles de bordure sont définis dans `maps.py`.

Le modèle utilise ces informations pour appliquer les règles de déplacement et de collision.

La définition d'une carte est donc séparée de la logique générale du jeu.

**### État dynamique**

L'état évolue pendant la partie.

Il contient :

```text
snake
direction
fruit
score
status
```

La liste `snake` contient toutes les positions occupées par le serpent.

Le premier élément correspond toujours à la tête :

```text
snake[0] → tête
snake[1] → segment
...
snake[-1] → queue
```

La longueur du serpent peut donc être déterminée avec le nombre d'éléments de cette liste.

Il n'est pas nécessaire de maintenir une variable `length` séparée.

---

# 2. Initialisation

Lorsqu'une nouvelle partie est créée :

1. La difficulté est définie.
2. L'identifiant de la carte est défini.
3. La définition de la carte correspondante est récupérée depuis `maps.py`.
4. Le serpent est placé au centre de la carte.
5. Sa longueur initiale est définie.
6. Sa direction est `null`.
7. Le score est initialisé à zéro.
8. Un fruit est généré sur une position valide.
9. Le statut de la partie est `waiting`.

Le serpent reste immobile jusqu'à la première commande de direction.

La carte sélectionnée et la difficulté restent inchangées pendant toute la partie.

---

# 3. Gestion de la direction

Lorsqu'une commande de direction est reçue :

1. Vérifier que la direction demandée est valide.
2. Vérifier qu'elle ne constitue pas un demi-tour immédiat.
3. Mettre à jour la direction si elle est valide.
4. Si la partie était dans l'état `waiting`, passer à l'état `running`.

Les directions possibles sont :

```text
UP
DOWN
LEFT
RIGHT
```

---

# 4. Boucle de jeu

Lorsque la partie est dans l'état `running`, les déplacements du serpent sont effectués à intervalles réguliers.

À chaque déplacement :

1. Déterminer la prochaine position de la tête.
2. Appliquer les règles de la carte.
3. Vérifier les collisions.
4. Déplacer le serpent.
5. Vérifier si un fruit est mangé.
6. Mettre à jour le score et la longueur si nécessaire.
7. Générer un nouveau fruit si nécessaire.
8. Continuer tant que la partie est active.

La fréquence des déplacements dépend de la difficulté configurée pour la partie.

---

# 5. Calcul de la prochaine position

La prochaine position de la tête dépend de :

* sa position actuelle ;
* la direction actuelle.

Exemple :

```text
Position actuelle : (5, 4)
Direction : RIGHT
Position suivante : (6, 4)
```

La représentation exacte des coordonnées est laissée à l'implémentation.

---

# 6. Gestion des bordures

Le comportement des bordures est défini dans la configuration de la carte située dans maps.py.

## Carte avec passage libre

Si le serpent dépasse une bordure, il réapparaît du côté opposé.

```text
droite → gauche
gauche → droite
haut   → bas
bas    → haut
```

Exemple :

```text
┌─────────────────┐
│                 │
│                 │
│              →→→│
└─────────────────┘
    ↓         ↓
┌─────────────────┐
│                 │
│                 │
│→→               │
└─────────────────┘
```

## Carte avec bordures

Si la prochaine position se trouve en dehors de la carte :

```text
collision → game_over
```
Le modèle applique le comportement défini par la carte sélectionnée.

---

# 7. Gestion des obstacles

Les obstacles de chaque carte sont définis dans `maps.py`.

Pour une carte contenant des obstacles :

1. Calculer la prochaine position.
2. Vérifier si cette position correspond à un obstacle défini pour la carte.
3. Si oui, la partie passe à `game_over`.
4. Sinon, le déplacement peut être effectué.

Les obstacles sont considérés comme des positions interdites.

Une carte peut ne contenir aucun obstacle.


---

# 8. Déplacement du serpent

Lors d'un déplacement normal :

1. Calculer la nouvelle position de la tête.
2. Ajouter cette position au début de `snake`.
3. Vérifier si un fruit est mangé.
4. Si aucun fruit n'est mangé, retirer la dernière position de `snake`.
5. Si un fruit est mangé, conserver la dernière position afin d'augmenter la longueur du serpent.

Exemple :

```text
Avant :

[HEAD][A][B]

Déplacement →

[NEW HEAD][HEAD][A]
```

La dernière position est normalement supprimée.

Lorsqu'un fruit est mangé :

```text
Avant :

[HEAD][A][B]

Déplacement + fruit →

[NEW HEAD][HEAD][A][B]
```

Le serpent gagne ainsi un segment.

---

# 9. Détection du fruit

Après avoir déterminé la nouvelle position de la tête :

1. Comparer cette position avec celle du fruit.
2. Si les positions correspondent, le fruit est consommé.
3. Augmenter le score.
4. Conserver la longueur supplémentaire du serpent.
5. Générer un nouveau fruit.

---

# 10. Score

La valeur du fruit dépend de la difficulté configurée pour la partie.

Les valeurs actuelles sont :

| Difficulté | Valeur du fruit |
| ---------- | --------------: |
| 1          |               4 |
| 2          |               5 |
| 3          |               6 |
| 4          |               7 |

La difficulté n'a pas besoin d'être enregistrée dans l'état dynamique.

Le `Game` peut utiliser sa configuration interne pour déterminer la valeur du fruit.

---

# 11. Génération d'un fruit

Lorsqu'un nouveau fruit doit être généré :

1. Choisir une position aléatoire.
2. Vérifier que la position se trouve dans les dimensions de la carte.
3. Vérifier que la position n'est pas un obstacle défini dans `maps.py`.
4. Vérifier qu'elle n'est pas occupée par le serpent.
5. Si la position est invalide, en générer une nouvelle.
6. Répéter jusqu'à obtenir une position valide.
7. Placer le fruit sur cette position.

---

# 12. Collision avec le serpent

La tête du serpent ne doit pas entrer en collision avec son propre corps.

Après avoir déterminé la nouvelle position de la tête, vérifier si cette position est occupée par un autre segment du serpent.

Si c'est le cas :

```text
collision → game_over
```

La logique doit tenir compte du déplacement de la queue afin d'éviter de considérer comme collision une position qui serait libérée au même déplacement.

---

# 13. Ordre des vérifications

L'ordre exact peut être adapté lors de l'implémentation, mais la logique générale doit respecter les étapes suivantes :

```text
Direction
   ↓
Prochaine position
   ↓
Règles de la carte
   ↓
Collision
   ↓
Déplacement
   ↓
Fruit ?
   ↓
Score / croissance
   ↓
Nouveau fruit
```

Cela permet de séparer clairement le calcul du déplacement, les collisions et la gestion des fruits.

---

# 14. Fin de partie

Lorsqu'une condition de fin est détectée :

1. Le statut passe à `game_over`.
2. Le déplacement du serpent s'arrête.
3. Le score final est conservé.
4. Le score peut être ajouté au tableau des scores.
5. Le frontend affiche l'écran de fin.
6. Le joueur peut recommencer ou retourner au menu.

Les principales conditions de fin sont :

* collision avec son propre corps ;
* collision avec une bordure ;
* collision avec un obstacle.

---

# 15. Tableau des scores

Lorsqu'une partie se termine :

1. Récupérer le score final de la partie.
2. Ajouter le score aux résultats de la session.
3. Trier les résultats du plus élevé au plus faible.
4. Conserver les dix meilleurs résultats.

Les scores sont uniquement conservés en mémoire.

---

# 16. Réinitialisation

Lorsqu'une nouvelle partie est créée avec la même configuration :

* le serpent est replacé au centre ;
* la longueur initiale est restaurée ;
* la direction revient à `null` ;
* le score revient à zéro ;
* un nouveau fruit est généré ;
* le statut revient à `waiting`.

La difficulté et la carte restent celles définies dans la configuration de la partie.

---

# 17. Fonctionnalités supplémentaires

Les fonctionnalités suivantes sont prévues comme extensions éventuelles :

* gros fruits ;
* compteur de fruits ;
* valeur décroissante ;
* différents skins ;
* sons ;
* musique ;
* animations supplémentaires.

Elles ne doivent pas compliquer l'implémentation des fonctionnalités principales.

### Exemple : gros fruit

Une logique possible serait :

```text
Fruit consommé
      ↓
Compteur de fruits
      ↓
Nombre requis atteint ?
      ↓
     Oui
      ↓
Gros fruit
      ↓
Durée limitée
      ↓
Consommé ? ── Oui → récompense
      │
      Non
      ↓
Expiration
```

Cette fonctionnalité pourra être implémentée séparément une fois le jeu de base terminé.

---

# 18. Principe général

Le modèle doit être responsable de la logique et de l'état du jeu.

Le contrôleur doit assurer la communication entre les requêtes reçues et le modèle.

Le frontend doit afficher l'état reçu et gérer les interactions avec le joueur.

La configuration d'une partie et son état dynamique doivent rester conceptuellement séparés :

```text
CONFIGURATION
├── difficulty
└── map

        ↓

GAME

        ↓

ÉTAT DYNAMIQUE
├── snake
├── direction
├── fruit
├── score
└── status
```

Cette séparation permet de limiter les données redondantes et de garder une structure simple.
