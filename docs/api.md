# API — Snake

## 1. Objectif

L'API permet au frontend de communiquer avec le backend.

Elle définit les échanges nécessaires entre l'interface utilisateur et la logique du jeu.

Les données sont échangées au format JSON.

L'API décrit **ce qui doit être échangé**, sans imposer la manière dont le backend doit être implémenté.

---

# 2. Configuration et état de la partie

Il faut distinguer deux types d'informations.

### Configuration de la partie

Ces informations sont définies au lancement de la partie et ne changent pas pendant celle-ci :

* difficulté ;
* identifiant de la carte.

Les définitions des cartes sont centralisées dans `maps.py`.

`maps.py` contient notamment :

* les dimensions communes des cartes ;
* les obstacles ;
* le comportement des bordures ;
* les informations propres à chaque carte.

La configuration sélectionnée est utilisée lors de la création de l'instance `Game`.

Exemple conceptuel :

```python
game = Game(
    difficulty=2,
    map_id=3
)
```

### État dynamique de la partie

Ces informations peuvent changer pendant la partie :

* positions du serpent ;
* direction ;
* position du fruit ;
* score ;
* statut de la partie.

Le serpent est représenté par une liste de positions.

Le **premier élément de la liste représente toujours la tête du serpent**.

Exemple :

```json
{
    "snake": [
        [5, 5],
        [4, 5],
        [3, 5]
    ]
}
```

Dans cet exemple :

```text
[5, 5] → tête
[4, 5] → deuxième segment
[3, 5] → queue
```

La longueur du serpent peut être obtenue à partir du nombre de positions dans `snake`.

Il n'est donc pas nécessaire de stocker une variable `length` séparément.

---

# 3. Liste des cartes

### `GET /maps`

Retourne les informations nécessaires au frontend pour afficher les cartes disponibles et leurs aperçus.

Les données sont basées sur les définitions présentes dans `maps.py`.

### Réponse

Exemple conceptuel :

```json
{
    "maps": [
        {
            "id": 1,
            "name": "Classique",
            "width": 20,
            "height": 15,
            "obstacles": [],
            "wrap": true
        },
        {
            "id": 2,
            "name": "Murs",
            "width": 20,
            "height": 15,
            "obstacles": [
                [5, 7],
                [6, 7],
                [7, 7]
            ],
            "wrap": false
        }
    ]
}
```

Les quatre cartes utilisent les mêmes dimensions.

Les positions des obstacles permettent au frontend de construire l'aperçu de chaque carte.

Le frontend ne doit pas avoir besoin de reproduire manuellement les définitions des cartes.

Cette route peut également être utilisée pour récupérer les informations nécessaires à l'affichage du menu de sélection des cartes.

---

# 4. Création d'une partie

### `POST /game/start`

Crée une nouvelle partie avec la difficulté et la carte sélectionnées.

### Requête

```json
{
    "difficulty": 2,
    "map_id": 3
}
```

### Paramètres

| Paramètre    | Type   | Description                          |
| ------------ | ------ | ------------------------------------ |
| `difficulty` | entier | Niveau de difficulté entre 1 et 4    |
| `map_id`     | entier | Identifiant de la carte entre 1 et 4 |

### Réponse

La réponse contient l'état initial de la partie.

```json
{
    "success": true,
    "game": {
        "snake": [
            [5, 5],
            [4, 5],
            [3, 5]
        ],
        "direction": null,
        "fruit": [10, 8],
        "score": 0,
        "status": "waiting"
    }
}
```

La difficulté et l'identifiant de la carte ne sont pas répétés dans l'état dynamique, car ils sont déjà associés à l'instance de la partie.

La définition complète de la carte peut être obtenue avec `GET /maps`.

---

# 5. État de la partie

### `GET /game/state`

Retourne l'état dynamique actuel de la partie.

### Réponse

```json
{
    "snake": [
        [5, 5],
        [4, 5],
        [3, 5]
    ],
    "direction": "RIGHT",
    "fruit": [10, 8],
    "score": 12,
    "status": "running"
}
```

### Champs

| Champ       | Type          | Description                               |
| ----------- | ------------- | ----------------------------------------- |
| `snake`     | liste         | Positions de tous les segments du serpent |
| `direction` | chaîne / null | Direction actuelle du serpent             |
| `fruit`     | position      | Position du fruit actuel                  |
| `score`     | entier        | Score actuel                              |
| `status`    | chaîne        | État actuel de la partie                  |

Le premier élément de `snake` représente toujours la tête.

La carte et la difficulté ne font pas partie de l'état dynamique.

---

# 6. Direction

### `POST /game/direction`

Transmet une nouvelle direction au jeu.

### Requête

```json
{
    "direction": "UP"
}
```

Les valeurs possibles sont :

```text
UP
DOWN
LEFT
RIGHT
```

Le backend doit vérifier que la direction est valide.

Il doit également empêcher le serpent d'effectuer un demi-tour immédiat.

Par exemple :

```text
Direction actuelle : RIGHT

UP      → autorisée
DOWN    → autorisée
RIGHT   → autorisée
LEFT    → interdite
```

---

# 7. Fin de partie

### `POST /game/end`

Indique que la partie est terminée.

Cette route peut être utilisée pour effectuer les opérations nécessaires à la fin de la partie, notamment la gestion du score.

Le score final doit être récupéré depuis l'état de la partie plutôt que d'être considéré comme une information indépendante fournie arbitrairement par le frontend.

Exemple :

```json
{
    "success": true
}
```

---

# 8. Tableau des scores

### `GET /scoreboard`

Retourne les meilleurs scores de la session.

### Réponse

```json
{
    "scores": [
        120,
        95,
        80,
        72,
        65,
        54,
        43,
        32,
        20,
        12
    ]
}
```

Le tableau contient au maximum dix résultats.

Les scores sont conservés uniquement en mémoire.

Aucune base de données n'est nécessaire.

---

# 9. Réinitialisation

### `POST /game/reset`

Réinitialise la partie actuelle.

Après une réinitialisation :

* le serpent retrouve sa configuration initiale ;
* le score revient à zéro ;
* une nouvelle position de fruit est générée ;
* la direction revient à `null` ;
* le statut revient à `waiting`.

La difficulté et la carte sélectionnées restent celles de la partie.

---

# 10. États possibles

Une partie peut avoir les états suivants :

```text
waiting
running
game_over
```

### `waiting`

La partie a été créée mais le serpent n'a pas encore commencé à se déplacer.

### `running`

Le serpent se déplace et la partie est active.

### `game_over`

Une condition de fin de partie a été détectée.

---

# 11. Gestion des erreurs

Le backend doit permettre au frontend de distinguer une requête réussie d'une requête incorrecte.

Exemple :

```json
{
    "success": false,
    "error": "Invalid difficulty"
}
```

Les erreurs peuvent notamment concerner :

* une difficulté invalide ;
* une carte invalide ;
* une direction invalide ;
* une partie inexistante ;
* une action impossible dans l'état actuel de la partie.

---

# 12. Principe général de communication

Pour la sélection d'une carte :

```text
Frontend
   ↓
GET /maps
   ↓
Controller
   ↓
maps.py
   ↓
Définitions des cartes
   ↓
Réponse JSON
   ↓
Frontend
   ↓
Aperçu des cartes
```

Pour le lancement et le fonctionnement d'une partie :

```text
Joueur
   ↓
Frontend
   ↓
Requête HTTP
   ↓
Controller
   ↓
Game / Model
   ↓
Modification de l'état
   ↓
Réponse JSON
   ↓
Frontend
   ↓
Affichage
```

Le frontend ne doit pas avoir besoin de connaître la manière dont le backend stocke ou modifie l'état interne de la partie.

---

# 13. Évolution de l'API

Cette documentation constitue le contrat initial entre le frontend et le backend.

Les développeurs peuvent proposer des modifications lorsqu'une décision technique nécessite une adaptation.

Toute modification importante de l'API doit être documentée afin que le frontend et le backend utilisent toujours le même contrat.
