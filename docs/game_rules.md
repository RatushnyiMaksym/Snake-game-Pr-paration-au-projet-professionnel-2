# Règles du jeu — Snake

## 1. Objectif

Le joueur contrôle un serpent qui se déplace sur une carte.

L'objectif est de manger des fruits afin d'augmenter son score et la longueur du serpent, tout en évitant les collisions.

La partie se termine lorsque le serpent entre en collision avec lui-même ou avec un élément de la carte qui provoque une collision.

---

## 2. Démarrage d'une partie

Lorsqu'une partie commence :

* Le serpent apparaît au centre de la carte.
* Le serpent possède une longueur initiale définie.
* Le serpent est immobile.
* Aucun déplacement n'est effectué tant que le joueur n'a pas choisi une direction.
* La difficulté et la carte sélectionnées dans le menu sont utilisées pour la partie.

La partie commence réellement lorsque le joueur effectue sa première commande de direction.

---

## 3. Déplacement du serpent

Le serpent se déplace continuellement dans la direction actuelle.

Le joueur peut modifier la direction du serpent à l'aide des touches directionnelles.

Le serpent ne peut pas effectuer un demi-tour instantané.

Par exemple, si le serpent se déplace vers la droite, il ne peut pas immédiatement se déplacer vers la gauche.

La vitesse du serpent dépend du niveau de difficulté sélectionné.

---

## 4. Difficulté

Le jeu possède quatre niveaux de difficulté.

| Niveau | Valeur d'un fruit |         Vitesse |
| ------ | ----------------: | --------------: |
| 1      |          4 points | vitesse de base |
| 2      |          5 points |          1,25 × |
| 3      |          6 points |          1,50 x |
| 4      |          7 points |          1,75 × |

Le niveau 1 est sélectionné par défaut.

Les valeurs exactes des multiplicateurs de vitesse des niveaux intermédiaires pourront être ajustées lors du développement.

---

## 5. Fruits

Un fruit apparaît sur une position libre de la carte.

Lorsqu'un serpent mange un fruit :

* Le joueur reçoit les points correspondant au niveau de difficulté.
* La longueur du serpent augmente.
* Un nouveau fruit apparaît à une position valide.

Le fruit ne peut pas apparaître :

* sur le serpent ;
* sur un obstacle ;
* sur une position qui n'est pas accessible dans la carte.

### Fonctionnalités supplémentaires

Les gros fruits, les différents skins de fruits et la diminution progressive de leur valeur sont considérés comme des fonctionnalités supplémentaires.

Ils pourront être ajoutés si le développement principal est terminé et que le temps disponible le permet.

---

## 6. Cartes

Le jeu doit proposer quatre cartes.

### Carte 1 — Passage libre

La carte possède une forme rectangulaire.

Les bords ne provoquent pas de collision.

Lorsqu'un serpent quitte la carte par un côté, il réapparaît du côté opposé.

Exemple :

```text
← sort à gauche    → réapparaît à droite
↑ sort en haut     ↓ réapparaît en bas
```

Cette carte est sélectionnée par défaut.

### Carte 2 — Bordures

La carte possède des murs sur ses quatre côtés.

Si la tête du serpent entre en collision avec un mur, la partie se termine.

### Carte 3 — Obstacles

La carte contient des obstacles internes.

Les obstacles provoquent une collision avec le serpent.

Le comportement des bordures dépend de la configuration définie pour cette carte.

### Carte 4 — Obstacles

La carte contient également des obstacles internes avec une disposition différente de la carte 3.

Le comportement des bordures dépend de la configuration définie pour cette carte.

---

## 7. Croissance du serpent

Chaque fruit mangé augmente la longueur du serpent d'un nombre constant de cases.

La longueur initiale du serpent et la quantité exacte d'augmentation doivent être définies dans l'implémentation.

---

## 8. Collisions

La partie se termine lorsque le serpent entre en collision avec :

* son propre corps ;
* un mur d'une carte avec bordures ;
* un obstacle.

Sur une carte avec passage libre, sortir d'un côté de la carte ne provoque pas de collision.

---

## 9. Score

Le score commence à zéro au début de chaque partie.

Le score augmente lorsqu'un fruit est mangé.

La valeur du fruit dépend du niveau de difficulté.

Le score est affiché pendant la partie.

---

## 10. Fin de partie

Lorsqu'une collision provoque la fin de la partie :

* Le déplacement du serpent s'arrête.
* Le score final est enregistré.
* Le joueur peut recommencer une partie.
* Le joueur peut également retourner au menu principal.

---

## 11. Tableau des scores

Le jeu conserve les dix meilleurs scores de la session.

Le tableau des scores contient au maximum dix résultats.

Les scores sont conservés uniquement en mémoire pendant l'utilisation de l'application.

Aucune base de données n'est nécessaire.

Lorsque le joueur quitte l'application, les scores sont supprimés.

---

## 12. Menu principal

Le menu principal doit proposer les cinq options suivantes :

1. **Jouer**
2. **Difficulté**
3. **Carte**
4. **Tableau des scores**
5. **Quitter**

### Jouer

Lance une partie avec les paramètres actuellement sélectionnés.

### Difficulté

Permet de sélectionner l'un des quatre niveaux de difficulté.

### Carte

Permet de sélectionner l'une des quatre cartes.

### Tableau des scores

Affiche les dix meilleurs scores de la session.

### Quitter

Ferme l'application et entraîne la suppression du tableau des scores conservé en mémoire.

---

## 13. Fonctionnalités optionnelles

Les fonctionnalités suivantes ne sont pas nécessaires au fonctionnement de base :

* différents skins de fruits ;
* gros fruits ;
* diminution de la valeur des gros fruits avec le temps ;
* sons ;
* musique ;
* animations supplémentaires ;
* effets visuels supplémentaires.

Ces fonctionnalités pourront être ajoutées après l'implémentation des fonctionnalités principales.
